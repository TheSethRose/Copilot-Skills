# Typescript - Common Patterns

Quick reference for common typescript patterns and usage.

## Code Patterns

### 1. Was this page helpful?Get StartedTS for the New ProgrammerTypeScript for JS ProgrammersTS for Java/C

```
Microsoft.AspNetCore.StaticFiles
```

### 2. ASP.NET CoreInstall ASP.NET Core and TypeScript First, install ASP.NET Core if you need it. This qui

```
Microsoft.AspNetCore.StaticFiles
```

### 3. Install ASP.NET Core and TypeScript First, install ASP.NET Core if you need it. This quick-start gui

```
Microsoft.AspNetCore.StaticFiles
```

### 4. Install ASP.NET Core and TypeScript First, install ASP.NET Core if you need it. This quick-start gui

```
Microsoft.AspNetCore.StaticFiles
```

### 5. First we need to tell TypeScript how to build. Right click on scripts and click New Item. Then choos

```
scripts
```

### 6. Was this page helpful?Get StartedTS for the New ProgrammerTypeScript for JS ProgrammersTS for Java/C

```
class
```

### 7. Classes Background Reading:Classes (MDN) TypeScript offers full support for the class keyword introd

```
class
```

### 8. Background Reading:Classes (MDN) TypeScript offers full support for the class keyword introduced in 

```
class
```

## Examples

### Example 1

```javascript
function sayHello() {  const compiler = (document.getElementById("compiler") as HTMLInputElement)    .value;  const framework = (document.getElementById("framework") as HTMLInputElement)    .value;  return `Hello from ${compiler} and ${framework}!`;}
```

### Example 2

```javascript
class Point {  x: number;  y: number;} const pt = new Point();pt.x = 0;pt.y = 0;
```

### Example 3

```python
import * as _ from "lodash";_.padStart("Hello TypeScript!", 20, " ");
```

### Example 4

```javascript
// 1. Select the div element using the id propertyconst app = document.getElementById("app");// 2. Create a new <p></p> element programmaticallyconst p = document.createElement("p");// 3. Add the text contentp.textContent = "Hello, World!";// 4. Append the p element to the div elementapp?.appendChild(p);
```

### Example 5

```javascript
interface Box {  height: number;  width: number;}interface Box {  scale: number;}let box: Box = { height: 5, width: 6, scale: 10 };
```


## Categories

See organized documentation in `references/`:

- `references/everyday_types.md` - Everyday Types
- `references/getting_started.md` - Getting Started
