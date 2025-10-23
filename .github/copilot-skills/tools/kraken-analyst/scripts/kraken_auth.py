#!/usr/bin/env python3
"""
kraken_auth.py - Kraken Analyst Skill: Authentication Module

Handles authentication for Kraken private API endpoints.
Provides signing of private requests using API key and secret.

Usage:
    from kraken_auth import KrakenAuth
    
    auth = KrakenAuth()
    if auth.is_authenticated():
        response = auth.query_private("Balance")

Environment Variables Required:
    KRAKEN_API_KEY - Your Kraken API key
    KRAKEN_PRIVATE_KEY - Your Kraken private key (base64 encoded)

Security Notes:
    - Never commit .env file with real credentials
    - API keys should have minimal required permissions
    - Use API key restrictions (IP whitelist, time limits)
"""

import os
import sys
import time
import hmac
import hashlib
import base64
import urllib.parse
import urllib.request
import json
from typing import Dict, Optional, Any
from pathlib import Path

# Load .env file manually if it exists (without requiring python-dotenv)
def load_env_file():
    """Load environment variables from .env file"""
    env_path = Path(__file__).parent.parent / '.env'
    if env_path.exists():
        with open(env_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    # Remove quotes if present
                    value = value.strip('"').strip("'")
                    os.environ[key.strip()] = value

# Load .env on module import
load_env_file()


class KrakenAuth:
    """Handles Kraken API authentication and private endpoint requests"""
    
    BASE_URL = "https://api.kraken.com"
    API_VERSION = "0"
    
    def __init__(self, api_key: Optional[str] = None, private_key: Optional[str] = None):
        """
        Initialize authentication handler
        
        Args:
            api_key: Kraken API key (or read from KRAKEN_API_KEY env var)
            private_key: Kraken private key base64 (or read from KRAKEN_PRIVATE_KEY env var)
        """
        self.api_key = api_key or os.getenv("KRAKEN_API_KEY", "")
        self.private_key = private_key or os.getenv("KRAKEN_PRIVATE_KEY", "")
        self.rate_limit = float(os.getenv("RATE_LIMIT", "0.5"))
        self.last_request_time = 0
    
    def is_authenticated(self) -> bool:
        """Check if API credentials are configured"""
        return bool(self.api_key and self.private_key)
    
    def _get_kraken_signature(self, urlpath: str, data: Dict[str, Any], nonce: int) -> str:
        """
        Generate Kraken API signature for private endpoints
        
        Args:
            urlpath: API endpoint path (e.g., "/0/private/Balance")
            data: POST data dictionary including nonce
            nonce: Unique nonce value
            
        Returns:
            Base64 encoded signature
        """
        # Encode data for signing
        postdata = urllib.parse.urlencode(data)
        encoded = (str(nonce) + postdata).encode()
        message = urlpath.encode() + hashlib.sha256(encoded).digest()
        
        # Create signature
        signature = hmac.new(
            base64.b64decode(self.private_key),
            message,
            hashlib.sha512
        )
        
        return base64.b64encode(signature.digest()).decode()
    
    def _rate_limit_wait(self):
        """Enforce rate limiting between requests"""
        elapsed = time.time() - self.last_request_time
        if elapsed < self.rate_limit:
            time.sleep(self.rate_limit - elapsed)
        self.last_request_time = time.time()
    
    def query_private(self, method: str, data: Optional[Dict[str, Any]] = None) -> Optional[Dict]:
        """
        Query a Kraken private API endpoint
        
        Args:
            method: API method name (e.g., "Balance", "OpenOrders")
            data: Optional POST parameters
            
        Returns:
            API response dictionary or None on error
        """
        if not self.is_authenticated():
            print("ERROR: API credentials not configured. Set KRAKEN_API_KEY and KRAKEN_PRIVATE_KEY in .env", 
                  file=sys.stderr)
            return None
        
        # Prepare request
        urlpath = f"/{self.API_VERSION}/private/{method}"
        url = f"{self.BASE_URL}{urlpath}"
        
        # Add nonce to data
        if data is None:
            data = {}
        data["nonce"] = str(int(time.time() * 1000))
        
        # Generate signature
        signature = self._get_kraken_signature(urlpath, data, int(data["nonce"]))
        
        # Prepare headers
        headers = {
            "API-Key": self.api_key,
            "API-Sign": signature,
            "Content-Type": "application/x-www-form-urlencoded"
        }
        
        # Make request
        self._rate_limit_wait()
        
        try:
            postdata = urllib.parse.urlencode(data).encode()
            request = urllib.request.Request(url, data=postdata, headers=headers)
            
            with urllib.request.urlopen(request, timeout=30) as response:
                response_data = json.loads(response.read().decode())
                
                # Check for API errors
                if response_data.get("error") and len(response_data["error"]) > 0:
                    print(f"ERROR: Kraken API error: {response_data['error']}", file=sys.stderr)
                    return None
                
                return response_data.get("result")
        
        except urllib.error.HTTPError as e:
            print(f"ERROR: HTTP {e.code} - {e.reason}", file=sys.stderr)
            return None
        except urllib.error.URLError as e:
            print(f"ERROR: Connection failed - {e.reason}", file=sys.stderr)
            return None
        except Exception as e:
            print(f"ERROR: {str(e)}", file=sys.stderr)
            return None
    
    def query_public(self, method: str, params: Optional[Dict[str, Any]] = None) -> Optional[Dict]:
        """
        Query a Kraken public API endpoint (no authentication required)
        
        Args:
            method: API method name (e.g., "OHLC", "Ticker")
            params: Optional query parameters
            
        Returns:
            API response dictionary or None on error
        """
        url = f"{self.BASE_URL}/{self.API_VERSION}/public/{method}"
        
        if params:
            query_string = urllib.parse.urlencode(params)
            url = f"{url}?{query_string}"
        
        self._rate_limit_wait()
        
        try:
            with urllib.request.urlopen(url, timeout=30) as response:
                response_data = json.loads(response.read().decode())
                
                if response_data.get("error") and len(response_data["error"]) > 0:
                    print(f"ERROR: Kraken API error: {response_data['error']}", file=sys.stderr)
                    return None
                
                return response_data.get("result")
        
        except urllib.error.HTTPError as e:
            print(f"ERROR: HTTP {e.code} - {e.reason}", file=sys.stderr)
            return None
        except urllib.error.URLError as e:
            print(f"ERROR: Connection failed - {e.reason}", file=sys.stderr)
            return None
        except Exception as e:
            print(f"ERROR: {str(e)}", file=sys.stderr)
            return None


if __name__ == "__main__":
    # Test authentication
    auth = KrakenAuth()
    
    if auth.is_authenticated():
        print("✓ API credentials configured", file=sys.stderr)
        print("Testing connection...", file=sys.stderr)
        
        # Test with Balance endpoint
        result = auth.query_private("Balance")
        if result:
            print("✓ Authentication successful", file=sys.stderr)
            print(json.dumps(result, indent=2))
        else:
            print("✗ Authentication failed", file=sys.stderr)
            sys.exit(1)
    else:
        print("✗ API credentials not found in environment", file=sys.stderr)
        print("Set KRAKEN_API_KEY and KRAKEN_PRIVATE_KEY in .env file", file=sys.stderr)
        sys.exit(1)
