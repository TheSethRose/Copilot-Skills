# React - Common Patterns

Quick reference for common react patterns and usage.

## Code Patterns

### 1. Learn ReactInstallationAdd React to an Existing ProjectIf you want to add some interactivity to your

```
example.com
```

### 2. If you want to add some interactivity to your existing project, you don’t have to rewrite it in Reac

```
example.com
```

### 3. If you want to add some interactivity to your existing project, you don’t have to rewrite it in Reac

```
example.com
```

### 4. If the entire content of your page was replaced by a “Hello, world!”, everything worked! Keep readin

```
import { createRoot } from 'react-dom/client';// Clear the existing HTML contentdocument.body.innerHTML = '<div id="app"></div>';// Render your React component insteadconst root = createRoot(document.getElementById('app'));root.render(<h1>Hello, world</h1>);
```

### 5. Instead, you probably want to render your React components in specific places in your HTML. Open you

```
id
```

### 6. Learn ReactAdding InteractivitySome things on the screen update in response to user input. For examp

```
<button>
```

### 7. Some things on the screen update in response to user input. For example, clicking an image gallery s

```
<button>
```

### 8. Some things on the screen update in response to user input. For example, clicking an image gallery s

```
<button>
```

## Examples

### Example 1

```python
import { createRoot } from 'react-dom/client';// Clear the existing HTML contentdocument.body.innerHTML = '<div id="app"></div>';// Render your React component insteadconst root = createRoot(document.getElementById('app'));root.render(<h1>Hello, world</h1>);
```

### Example 2

```javascript
const [index, setIndex] = useState(0);const [showMore, setShowMore] = useState(false);
```

### Example 3

```javascript
const [x, setX] = useState(0);const [y, setY] = useState(0);
```

### Example 4

```javascript
const [position, setPosition] = useState({ x: 0, y: 0 });
```

### Example 5

```javascript
function ProblematicComponent() {  "use no memo"; // Skip compilation for this component  // ... rest of component}
```

### Example 6

```javascript
const ref = useRef(0);
```

### Example 7

```javascript
function Form() {  const [firstName, setFirstName] = useState('Taylor');  const [lastName, setLastName] = useState('Swift');  // 🔴 Avoid: redundant state and unnecessary Effect  const [fullName, setFullName] = useState('');  useEffect(() => {    setFullName(firstName + ' ' + lastName);  }, [firstName, lastName]);  // ...}
```

### Example 8

```javascript
function MessageComponent({ messagePromise }) {  const message = use(messagePromise);  const theme = use(ThemeContext);  // ...}
```

### Example 9

```javascript
function ImageGallery() {  const [index, setIndex] = useState(0);  // ...
```

### Example 10

```javascript
function Button() {  const theme = useContext(ThemeContext);  // ...
```


## Categories

See organized documentation in `references/`:

- `references/learn.md` - Learn
- `references/other.md` - Other
- `references/reference.md` - Reference
