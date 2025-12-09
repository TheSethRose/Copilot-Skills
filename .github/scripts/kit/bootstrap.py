import os
import json
import time
import argparse
import subprocess
from pathlib import Path
from kit import Repository

# Configuration
REPO_CACHE_DIR = os.path.expanduser("~/.kit_cache/repos")
ANALYSIS_DIR = os.path.join(os.getcwd(), ".kit-analysis")

def get_git_remote():
    """Auto-detect git remote origin URL"""
    try:
        result = subprocess.run(
            ["git", "config", "--get", "remote.origin.url"],
            capture_output=True,
            text=True,
            timeout=5,
            cwd=os.getcwd()
        )
        if result.returncode == 0:
            url = result.stdout.strip()
            if url:
                return url
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass
    return None

# Ensure directories exist
os.makedirs(REPO_CACHE_DIR, exist_ok=True)
os.makedirs(ANALYSIS_DIR, exist_ok=True)

def analyze_repository(repo_path: str, output_dir: str, use_cache: bool = True) -> dict:
    """
    Analyze a repository (local path only).
    
    Args:
        repo_path: Path to local repo (must be local, not URL)
        output_dir: Directory to save analysis files
        use_cache: Whether to use persistent cache (ignored for local)
        
    Returns:
        Dictionary with analysis statistics
    """
    print(f"🚀 Analyzing repository: {repo_path}")
    start_time = time.time()
    
    # Always use local path
    # Remote URLs cause file path resolution issues
    if repo_path.startswith("http"):
        print(f"❌ Error: Remote URLs not supported. Use local path instead.")
        exit(1)
    
    repo = Repository(repo_path)
    
    stats = {}
    
    # Generate file tree
    print("📊 Generating file tree...")
    file_tree = repo.get_file_tree()
    file_tree_path = os.path.join(output_dir, "file_tree.json")
    with open(file_tree_path, "w") as f:
        json.dump(file_tree, f, indent=2)
    stats["files"] = len(file_tree)
    print(f"✅ File tree saved ({len(file_tree)} files)")

    # Extract symbols
    print("🔍 Extracting symbols...")
    symbols = repo.extract_symbols()
    
    # Convert symbols to JSON-serializable format
    serialized_symbols = []
    
    for sym in symbols:
        # Handle both object and dict (just in case)
        if isinstance(sym, dict):
            # It's a dict
            name = sym.get('name')
            kind = sym.get('type')
            file_path = sym.get('file')
            line = sym.get('start_line', 0)
            
            serialized_symbols.append({
                "name": name,
                "kind": kind,
                "file": file_path,
                "line": line
            })
        else:
            # It's an object (fallback)
            serialized_symbols.append({
                "name": sym.name,
                "kind": sym.kind,
                "file": sym.file_path,
                "line": sym.range.start.line,
            })

    symbols_path = os.path.join(output_dir, "symbols.json")
    with open(symbols_path, "w") as f:
        json.dump(serialized_symbols, f, indent=2)
    stats["symbols"] = len(serialized_symbols)
    print(f"✅ {len(serialized_symbols)} symbols saved")

    # Create summary markdown
    summary_path = os.path.join(output_dir, "summary.md")
    with open(summary_path, "w") as f:
        f.write(f"# Codebase Analysis Summary\n\n")
        f.write(f"**Generated:** {time.ctime()}\n")
        f.write(f"**Repository:** {repo_path}\n")
        f.write(f"**Total Files:** {len(file_tree)}\n")
        f.write(f"**Total Symbols:** {len(serialized_symbols)}\n\n")
        f.write("## Top Files by Symbol Count\n")
        
        # Simple stats
        from collections import Counter
        file_counts = Counter([s['file'] for s in serialized_symbols])
        for file, count in file_counts.most_common(10):
            f.write(f"- `{file}`: {count} symbols\n")

    print(f"✅ Summary saved")
    
    elapsed = time.time() - start_time
    stats["time_seconds"] = elapsed
    
    return stats

def main():
    parser = argparse.ArgumentParser(
        description="Analyze a repository (local or remote) using Kit and generate analysis files."
    )
    parser.add_argument(
        "--repo",
        default=None,
        help="Repository path (local only). Default: current directory"
    )
    parser.add_argument(
        "--output",
        default=ANALYSIS_DIR,
        help=f"Output directory for analysis files. Default: {ANALYSIS_DIR}"
    )
    parser.add_argument(
        "--no-cache",
        action="store_true",
        help="Disable persistent cache for remote repositories"
    )
    parser.add_argument(
        "--cache-dir",
        default=REPO_CACHE_DIR,
        help=f"Directory to store remote repository cache. Default: {REPO_CACHE_DIR}"
    )
    parser.add_argument(
        "--clear-cache",
        action="store_true",
        help="Clear the remote repository cache before running"
    )
    
    args = parser.parse_args()
    
    # Use local repo by default (faster), only use git remote if explicitly requested
    if args.repo is None:
        args.repo = os.getcwd()
        print(f"📂 Using local repository: {args.repo}")
    
    # Handle cache clearing
    if args.clear_cache:
        print(f"🗑️  Clearing cache: {args.cache_dir}")
        import shutil
        if os.path.exists(args.cache_dir):
            shutil.rmtree(args.cache_dir)
        os.makedirs(args.cache_dir, exist_ok=True)
        print("✅ Cache cleared")
    
    # Ensure output directory exists
    os.makedirs(args.output, exist_ok=True)
    
    # Run analysis
    try:
        stats = analyze_repository(
            args.repo,
            args.output,
            use_cache=not args.no_cache
        )
        
        print(f"\n✨ Analysis complete!")
        print(f"   📁 Files: {stats['files']}")
        print(f"   🔤 Symbols: {stats['symbols']}")
        print(f"   ⏱️  Time: {stats['time_seconds']:.2f}s")
        print(f"   📂 Output: {args.output}")
        
        if args.repo.startswith("http") and not args.no_cache:
            print(f"   💾 Cache: {args.cache_dir}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        exit(1)

if __name__ == "__main__":
    main()
