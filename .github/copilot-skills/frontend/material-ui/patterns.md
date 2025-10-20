# Material-Ui - Common Patterns

Quick reference for common material-ui patterns and usage.

## Code Patterns

### 1. + How to customizeLearn how to customize Material UI components by taking advantage of different str

```
sx
```

### 2. How to customizeLearn how to customize Material UI components by taking advantage of different strat

```
sx
```

### 3. Learn how to customize Material UI components by taking advantage of different strategies for specif

```
sx
```

### 4. Overriding nested component stylesTo customize a specific part of a component, you can use the class

```
sx
```

### 5. The styles injected into the DOM by Material UI rely on class names that all follow a standard patte

```
[hash]-Mui[Component name]-[name of the slot]
```

### 6. + InstallationInstall Material UI, the world's most popular React UI framework. Default installation

```
npm install @mui/material @emotion/react @emotion/styled
```

### 7. Google Web FontsTo install the Material Icons font in your project using the Google Web Fonts CDN, a

```
<head />
```

### 8. To use the font Icon component, you must first add the Material Icons font. Here are some instructio

```
Icon
```

## Examples

### Example 1

```tsx
<Slider defaultValue={30} sx={{ width: 300, color: 'success.main' }} />
```

### Example 2

```tsx
<Slider
  defaultValue={30}
  sx={{
    width: 300,
    color: 'success.main',
    '& .MuiSlider-thumb': {
      borderRadius: '1px',
    },
  }}
/>
```

### Example 3

```bash
npm install @mui/material @emotion/react @emotion/styled
```

### Example 4

```json
"peerDependencies": {
  "react": "^17.0.0 || ^18.0.0 || ^19.0.0",
  "react-dom": "^17.0.0 || ^18.0.0 || ^19.0.0"
},
```


## Categories

See organized documentation in `references/`:

- `references/material-ui.md` - Material-Ui
- `references/other.md` - Other
- `references/store.md` - Store
