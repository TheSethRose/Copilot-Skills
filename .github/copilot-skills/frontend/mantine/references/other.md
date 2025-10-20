# Mantine - Other

**Pages**: 33

---

## 6.x to 7.x migration | Mantine

**URL**: https://mantine.dev/guides/6x-to-7x/

**Contents**:
- 6.x → 7.x migration guide
- Migration to @mantine/emotion
  - createStyles and Global component
  - sx and styles props
  - theme.colorScheme
- Migration to CSS modules
  - createStyles
  - sx prop

This guide is intended to help you migrate your project styles from 6.x to 7.x. It is not intended to be a comprehensive guide to all the changes in 7.x. For that, please see the 7.0.0 changelog.

@mantine/emotion package is available starting from version 7.9. If you do not want to use CSS modules, have a lot of styles created with createStyles, sx and styles props, or just prefer CSS-in-JS syntax, you can migrate to @mantine/emotion. To view the full documentation for @mantine/emotion package, visit this page.

createStyles function and Global component are no longer available in @mantine/core package. Change imports to @mantine/emotion:

sx and styles props available in 7.x the same way as in 6.x after setup:

In v7 color scheme value is managed by MantineProvider, theme object no longer includes colorScheme property. Although it is still possible to access color scheme value in components with useMantineColorScheme hook, it is not recommended to base your styles on its value. Instead, use light/dark utilities.

Example of 6.x createStyles with theme.colorScheme migration to 7.0:

Before getting started, it is recommended to go through styles documentation. Most notable parts:

Note that this guide assumes that you have postcss-preset-mantine installed and configured in your project.

createStyles function is no longer available in 7.0. Use CSS Modules instead.

sx and prop is no longer available in 7.0. Use className or style prop instead.

Nested selectors are not supported in style prop, use className instead:

styles prop no longer supports nested selectors. Use classNames instead to apply styles to nested elements.

Regular selectors are still supported:

Global component and global styles on theme are not available in 7.0. Instead, create a global stylesheet (.css file) and import it in your application entry point.

All theme properties are now available as CSS variables. It is recommended to use CSS variables instead of referencing theme object in styles.

*[Content truncated - see full docs]*

**Examples**:

```python
// 6.x
import { createStyles, Global } from '@mantine/core';

// 7.x
import { createStyles, Global } from '@mantine/emotion';
```

```python
// 6.x and 7.x, no changes
import { Box, Button } from '@mantine/core';

function Demo() {
  return (
    <>
      <Box
        sx={(theme) => ({ backgroundColor: theme.colors.red[5] })}
      />
      <Button styles={{ root: { height: 50 } }} />
    </>
  );
}
```

```python
// 6.x
import { createStyles } from '@mantine/core';

const useStyles = createStyles((theme) => ({
  root: {
    backgroundColor:
      theme.colorScheme === 'dark'
        ? theme.colors.dark[6]
        : theme.colors.gray[0],
    color: theme.colorScheme === 'dark' ? theme.white : theme.black,
  },
}));
```

---

## Calendar | Mantine

**URL**: https://mantine.dev/dates/calendar/

**Contents**:
- Calendar
- Usage
- Custom date pickers
- Static prop

Base component for custom date pickers

Use Calendar component to create custom date pickers if DatePicker component does not meet your requirements. Calendar supports all DatePicker props and some other props that are listed in props table – check it out to learn about all component features.

By default, Calendar works the same way as DatePicker component but does not include any logic of dates selection:

Use Calendar as a base for custom date pickers. For example, you can create a date picker that allows user to pick three or less dates:

Another custom date picker example – week picker:

Set static prop to display a calendar that user cannot interact with. It is useful when you want to display data with in calendar view but do not want it to be interactive.

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { Calendar } from '@mantine/dates';

function Demo() {
  return <Calendar />;
}
```

```python
import dayjs from 'dayjs';
import { useState } from 'react';
import { Calendar } from '@mantine/dates';

function Demo() {
  const [selected, setSelected] = useState<string[]>([]);
  const handleSelect = (date: string) => {
    const isSelected = selected.some((s) => dayjs(date).isSame(s, 'date'));
    if (isSelected) {
      setSelected((current) => current.filter((d) => !dayjs(d).isSame(date, 'date')));
    } else if (selected.length < 3) {
      setSelected((current) => [...current, date]);
 
...
```

```python
import dayjs from 'dayjs';
import { useState } from 'react';
import { Calendar } from '@mantine/dates';

function getDay(date: string) {
  const day = dayjs(date).day();
  return day === 0 ? 6 : day - 1;
}

function startOfWeek(date: string) {
  return dayjs(date)
    .subtract(getDay(date) + 1, 'day')
    .toDate();
}

function endOfWeek(date: string) {
  return dayjs(date)
    .add(6 - getDay(date), 'day')
    .endOf('day')
    .toDate();
}

function isInWeekRange(date: string, value: string |
...
```

---

## Carousel | Mantine

**URL**: https://mantine.dev/x/carousel/

**Contents**:
- Carousel
- Installation
- Do not forget to import styles
- Documentation demos
- Usage
- Options
- Embla options
- Size and gap

Embla based carousel component

After installation import package styles at the root of your application:

Followed installation instructions above but something is not working (Carousel slides are rendered vertically, no controls or indicators)? You've fallen into the trap of not importing carousel styles! To fix the issue, import carousel styles at the root of your application:

Demos on this page use a blue background color for demonstration purposes. To simplify the demos, background color and other demo-only styles are not included in the code. If you copy-paste demo code into your project, it will not have a blue background color.

@mantine/carousel package is based on embla carousel:

You can pass configuration options directly to embla carousel with emblaOptions prop. You can find embla options description in embla options reference.

Example of passing loop, dragFree and align options:

Set slideSize and slideGap on Carousel component to control size and gap of every slide:

slideSize and slideGap props work the same way as style props, you can pass an object with values for different breakpoints:

To use container queries instead of media queries, set type="container". With container queries, slides size and gap will be adjusted based on the container width, not the viewport width.

Note that, when using container queries, slideSize and slideGap props cannot reference theme.breakpoints values in keys. It is required to use exact px or em values.

To see how the slides size and gap changes, resize the root element of the demo with the resize handle located at the bottom right corner of the demo:

dragFree will disable slides snap points – user will be able to stop dragging at any position:

Carousel with orientation="vertical" requires height prop to be set:

You can replace default next/previous controls icons with any React nodes:

Set height="100%" to make Carousel take 100% height of the container. Note that in this case:

You can get embla instance wit

*[Content truncated - see full docs]*

**Examples**:

```text
yarn add embla-carousel@^8.5.2 embla-carousel-react@^8.5.2 @mantine/carousel
```

```text
npm install embla-carousel@^8.5.2 embla-carousel-react@^8.5.2 @mantine/carousel
```

```text
import '@mantine/core/styles.css';
// ‼️ import carousel styles after core package styles
import '@mantine/carousel/styles.css';
```

---

## CodeHighlight | Mantine

**URL**: https://mantine.dev/x/code-highlight/

**Contents**:
- CodeHighlight
- Installation
- Example
- Adapters
- Usage with shiki
- Usage with highlight.js
- Create custom adapter
- Copy button

Highlight code with shiki or highlight.js

After installation import package styles at the root of your application:

CodeHighlight component is used to display code snippets with syntax highlighting. It provides a flexible adapter system that allows using any code highlighting library of your choice.

Example of code highlighting with shiki:

@mantine/code-highlight package does not depend on any specific code highlighting library. You can choose one of the default adapters provided by the package or create your own.

Shiki library provides the most advanced syntax highlighting for TypeScript and CSS/Sass code. It uses textmate grammars to highlight code (same as in VSCode). Shiki adapter is recommended if you need to highlight advanced TypeScript (generics, jsx nested in props) or CSS code (custom syntaxes, newest features). Shiki adapter is used for all code highlighting in Mantine documentation.

To use shiki adapter you need to install shiki package:

Then wrap your app with CodeHighlightAdapterProvider and provide createShikiAdapter as adapter prop:

After that, you can use CodeHighlight component in your application:

All further code highlighting examples on this page are using shiki adapter.

Highlight.js provides less accurate highlighting compared to shiki, but it has smaller bundle size and better performance. Choose highlight.js adapter if you need to highlight basic JavaScript, HTML, and CSS code.

To use highlight.js adapter you need to install highlight.js package:

Then wrap your app with CodeHighlightAdapterProvider and provide createHighlightJsAdapter as adapter prop:

Then you need to add styles of one of the highlight.js themes to your application. You can do that by importing css file from highlight.js package or adding it via CDN link to the head of your application:

After that, you can use CodeHighlight component in your application.

You can create a custom adapter if you want to enhance the default behavior of the code highlighting or use 

*[Content truncated - see full docs]*

**Examples**:

```text
yarn add @mantine/code-highlight
```

```text
npm install @mantine/code-highlight
```

```text
import '@mantine/core/styles.css';
// ‼️ import code-highlight styles after core package styles
import '@mantine/code-highlight/styles.css';
```

---

## Color schemes | Mantine

**URL**: https://mantine.dev/theming/color-schemes/

**Contents**:
- Color schemes
- data-mantine-color-scheme attribute
- use-mantine-color-scheme hook
- use-computed-color-scheme hook
- Transitions during color scheme change
- Color scheme value caveats
- ColorSchemeScript
- Auto color scheme

MantineProvider manages color scheme context in your application. You can configure the default color scheme value with defaultColorScheme prop, possible values are light, dark and auto (system color scheme is used). The default value is light.

When the MantineProvider is mounted, it sets a data-mantine-color-scheme attribute on the <html /> element to the value that the user has selected previously or to the value of defaultColorScheme prop. The data-mantine-color-scheme attribute is used in all components' styles to determine which colors the component should use.

useMantineColorScheme hook can be used to get and set current color scheme value:

useComputedColorScheme returns a computed color scheme value, it returns either light or dark. It can be used to implement color scheme toggle logic:

By default, transitions on all elements are disabled when color scheme changes to avoid inconsistent animations. To enable transitions during color scheme change, set keepTransitions: true option on useMantineColorScheme hook:

By default, the color scheme value is stored in local storage, and its value is saved in state before the component is mounted to avoid flash of inaccurate color scheme. This means that color scheme value can be different on client and server, as server does not have access to local storage and always uses the default value.

If you have server side rendering in your application (for example, if you use Next.js or React Router), then you cannot use colorScheme value in your application to avoid hydration issues. Instead, you can use dark and light mixins from postcss-preset-mantine to generate styles that will hide elements based on color scheme value:

colorScheme for client only applications

You can safely use colorScheme value in client only applications (for example, Vite or create-react-app applications). In this case, there is no hydration, and thus hydration error cannot occur.

ColorSchemeScript component renders script tag that sets data-m

*[Content truncated - see full docs]*

**Examples**:

```python
import { MantineProvider } from '@mantine/core';

function Demo() {
  return (
    <MantineProvider defaultColorScheme="dark">
      {/* Your app here */}
    </MantineProvider>
  );
}
```

```javascript
function useMantineColorScheme(): {
  /** Current color scheme value */
  colorScheme: 'dark' | 'light' | 'auto';

  /** Sets colors scheme to given value */
  setColorScheme: (colorScheme: 'dark' | 'light' | 'auto') => void;

  /** Toggle color scheme to the opposite value, if value is 'auto', color scheme is inferred from the OS settings */
  toggleColorScheme: () => void;

  /** Clears color scheme value from storage and sets it to `defaultColorScheme` */
  clearColorScheme: () => void;
};
```

```python
import { useMantineColorScheme, Button, Group } from '@mantine/core';

function Demo() {
  const { setColorScheme, clearColorScheme } = useMantineColorScheme();

  return (
    <Group>
      <Button onClick={() => setColorScheme('light')}>Light</Button>
      <Button onClick={() => setColorScheme('dark')}>Dark</Button>
      <Button onClick={() => setColorScheme('auto')}>Auto</Button>
      <Button onClick={clearColorScheme}>Clear</Button>
    </Group>
  );
}
```

---

## Colors | Mantine

**URL**: https://mantine.dev/theming/colors/

**Contents**:
- Colors
- Adding extra colors
- Virtual colors
- colorsTuple
- Supported color formats
- primaryColor
- primaryShade
- Color prop

Mantine uses open-color in default theme with some additions. Each color has 10 shades.

Colors are exposed on the theme object as an array of strings, you can access color shade by color name and index (0-9), colors with larger index are darker:

Colors are also exposed as CSS variables:

You can add any number of extra colors to theme.colors object. This will allow you to use them in all components that support color prop, for example Button, Badge and Switch.

Colors override must include at least 10 shades per color. Otherwise, you will get a TypeScript error and some variants will not have proper colors. If you only have one color value, you can either pick the remaining colors manually or use the colors generator tool.

You can add more than 10 shades per color: these values will not be used by Mantine components with the default colors resolver, but you can still reference them by index, for example, color="blue.11".

Virtual color is a special color which values should be different for light and dark color schemes. To define a virtual color, use virtualColor function which accepts an object with the following properties as a single argument:

To see the demo in action, switch between light and dark color schemes (Ctrl + J):

Use colorsTuple function to:

You can use the following color formats in theme.colors:

Example of adding oklch color to theme:

theme.primaryColor is a key of theme.colors, it is used:

CSS color values at theme.primaryColor

Value of theme.primaryColor must be a key of theme.colors object. For example, blue, orange or green. You cannot assign CSS color values, for example, the following code will throw an error during theme merging:

theme.primaryShade is a number from 0 to 9. It determines which shade will be used for the components that have color prop.

You can also customize primary shade for dark and light color schemes separately:

Components that support changing their color have color prop. This prop supports the following valu

*[Content truncated - see full docs]*

**Examples**:

```python
import { useMantineTheme } from '@mantine/core';

function Demo() {
  const theme = useMantineTheme();

  return (
    <div
      style={{
        backgroundColor: theme.colors.blue[1],
        color: theme.colors.blue[9],
      }}
    >
      This is a blue theme
    </div>
  );
}
```

```text
.demo {
  color: var(--mantine-color-red-5);
  background: var(--mantine-color-grape-9);
  border: 1px solid var(--mantine-color-blue-1);
}
```

```python
import { Group, Button, MantineProvider, createTheme } from '@mantine/core';

const theme = createTheme({
  colors: {
    'ocean-blue': ['#7AD1DD', '#5FCCDB', '#44CADC', '#2AC9DE', '#1AC2D9', '#11B7CD', '#09ADC3', '#0E99AC', '#128797', '#147885'],
    'bright-pink': ['#F0BBDD', '#ED9BCF', '#EC7CC3', '#ED5DB8', '#F13EAF', '#F71FA7', '#FF00A1', '#E00890', '#C50E82', '#AD1374'],
  },
});

function Demo() {
  return (
    <MantineProvider theme={theme}>
      <Group>
        <Button color="ocean-blu
...
```

---

## Combobox examples | Mantine

**URL**: https://mantine.dev/combobox/?e=BasicSelect

---

## Contributing to Mantine | Mantine

**URL**: https://mantine.dev/contribute/

**Contents**:
- Contributing to Mantine
- Ways to contribute
- Contributing workflow
- Get started with Mantine locally
- npm scripts
  - Development scripts
  - Testing scripts
  - Docs scripts

First of all, thank you for showing interest in contributing to Mantine! All your contributions are extremely valuable to the project!

All npm scripts are located at main package.json. Individual packages do not have dedicated scripts.

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

---

## DateInput | Mantine

**URL**: https://mantine.dev/dates/date-input/

**Contents**:
- DateInput
- DatePicker props
- Usage
- Value format
- Date parser
- Allow clear
- Min and max date
- Disabled state

DateInput supports most of the DatePicker props, read through DatePicker documentation to learn about all component features that are not listed on this page.

Use valueFormat prop to change dayjs format of value label. To use some custom formats, you need to enable custom parse format plugin:

Example of using DateInput with custom format:

Use dateParser prop to replace default date parser. Parser function accepts user input (string) and must return Date object:

Set clearable prop to allow removing value from the input. Input will be cleared if user selects the same date in dropdown or clears input value:

Set minDate and maxDate props to define min and max dates. If date that is after maxDate or before minDate is entered, then it will be considered invalid and input value will be reverted to last known valid date value.

DateInput component supports Input and Input.Wrapper components features and all input element props. DateInput documentation does not include all features supported by the component – see Input documentation to learn about all available features.

If DateInput is used without label prop, it will not be announced properly by screen reader:

Set aria-label to make the input accessible. In this case label will not be visible, but screen reader will announce it:

If label prop is set, input will be accessible it is not required to set aria-label:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { useState } from 'react';
import { DateInput } from '@mantine/dates';

function Demo() {
  const [value, setValue] = useState<string | null>(null);
  return (
    <DateInput
      value={value}
      onChange={setValue}
      label="Date input"
      placeholder="Date input"
    />
  );
}
```

```python
// Do this once in your application root file
import dayjs from 'dayjs';
import customParseFormat from 'dayjs/plugin/customParseFormat';

dayjs.extend(customParseFormat);
```

```python
import { DateInput } from '@mantine/dates';

function Demo() {
  return <DateInput valueFormat="YYYY MMM DD" label="Date input" placeholder="Date input" />;
}
```

---

## DatePickerInput | Mantine

**URL**: https://mantine.dev/dates/date-picker-input/

**Contents**:
- DatePickerInput
- DatePicker props
- Usage
- Multiple dates
- Dates range
- Presets
- Open picker in modal
- Value format

Date, multiple dates and dates range picker input

DatePickerInput supports most of the DatePicker props, read through DatePicker documentation to learn about all component features that are not listed on this page.

Set type="multiple" to allow user to pick multiple dates:

Set type="range" to allow user to pick dates range:

Use presets prop to add custom date presets. Presets are displayed next to the calendar:

To use presets with type="range", define value a tuple of two dates:

By default, DatePicker is rendered inside Popover. You can change that to Modal by setting dropdownType="modal":

Use valueFormat prop to change dayjs format of value label:

valueFormatter is a more powerful alternative to valueFormat prop. It allows formatting value label with a custom function. The function is the same for all component types (default, multiple and range) – you need to perform additional checks inside the function to handle different types.

Example of using a custom formatter function with type="multiple":

Set clearable prop to display clear button in the right section. Note that if you set rightSection prop, clear button will not be displayed.

DatePickerInput component supports Input and Input.Wrapper components features and all button element props. DatePickerInput documentation does not include all features supported by the component – see Input documentation to learn about all available features.

If DatePickerInput is used without label prop, it will not be announced properly by screen reader:

Set aria-label to make the input accessible. In this case label will not be visible, but screen reader will announce it:

If label prop is set, input will be accessible it is not required to set aria-label:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { useState } from 'react';
import { DatePickerInput } from '@mantine/dates';

function Demo() {
  const [value, setValue] = useState<string | null>(null);
  return (
    <DatePickerInput
      label="Pick date"
      placeholder="Pick date"
      value={value}
      onChange={setValue}
    />
  );
}
```

```python
import { useState } from 'react';
import { DatePickerInput } from '@mantine/dates';

function Demo() {
  const [value, setValue] = useState<string[]>([]);
  return (
    <DatePickerInput
      type="multiple"
      label="Pick dates"
      placeholder="Pick dates"
      value={value}
      onChange={setValue}
    />
  );
}
```

```python
import { useState } from 'react';
import { DatePickerInput } from '@mantine/dates';

function Demo() {
  const [value, setValue] = useState<[string | null, string | null]>([null, null]);
  return (
    <DatePickerInput
      type="range"
      label="Pick dates range"
      placeholder="Pick dates range"
      value={value}
      onChange={setValue}
    />
  );
}
```

---

## DatePicker | Mantine

**URL**: https://mantine.dev/dates/date-picker/

**Contents**:
- DatePicker
- Usage
- Allow deselect
- Multiple dates
- Dates range
- Single date in range
- Presets
- Default date

Inline date, multiple dates and dates range picker

Set allowDeselect to allow user to deselect current selected date by clicking on it. allowDeselect is disregarded when type prop is range or multiple. When date is deselected onChange is called with null.

Set type="multiple" to allow user to pick multiple dates:

Set type="range" to allow user to pick dates range:

By default, it is not allowed to select single date as range – when user clicks the same date second time it is deselected. To change this behavior set allowSingleDateInRange prop. allowSingleDateInRange is ignored when type prop is not range.

Use presets prop to add custom date presets. Presets are displayed next to the calendar:

To use presets with type="range", define value a tuple of two dates:

Use defaultDate prop to set date value that will be used to determine which year should be displayed initially. For example to display 2015 February month set defaultDate={new Date(2015, 1)}. If value is not specified, then defaultDate will use new Date(). Day, minutes and seconds are ignored in provided date object, only year and month data is used – you can specify any date value.

Note that if you set date prop, then defaultDate value will be ignored.

Set date, and onDateChange props to make currently displayed month, year and decade controlled. By doing so, you can customize date picking experience, for example, when user selects first date in range, you can add one month to the current date value:

Set defaultLevel prop to configure initial level that will be displayed:

Set hideOutsideDates prop to remove all dates that do not belong to the current month:

Set withWeekNumbers prop to display week numbers:

Set firstDayOfWeek prop to configure first day of week. The prop accepts number from 0 to 6, where 0 is Sunday and 6 is Saturday. Default value is 1 – Monday. You can also configure this option for all components with DatesProvider.

Set hideWeekdays prop to hide weekdays names:

Use weekendDays p

*[Content truncated - see full docs]*

**Examples**:

```python
import { useState } from 'react';
import { DatePicker } from '@mantine/dates';

function Demo() {
  const [value, setValue] = useState<string | null>(null);
  return <DatePicker value={value} onChange={setValue} />;
}
```

```python
import { useState } from 'react';
import { DatePicker } from '@mantine/dates';

function Demo() {
  const [value, setValue] = useState<string | null>(null);
  return <DatePicker allowDeselect value={value} onChange={setValue} />;
}
```

```python
import { useState } from 'react';
import { DatePicker } from '@mantine/dates';

function Demo() {
  const [value, setValue] = useState<string[]>([]);
  return <DatePicker type="multiple" value={value} onChange={setValue} />;
}
```

---

## DateTimePicker | Mantine

**URL**: https://mantine.dev/dates/date-time-picker/

**Contents**:
- DateTimePicker
- DatePicker props
- Usage
- With seconds
- Presets
- TimePicker props
- Value format
- Disabled state

Capture datetime from the user

DateTimePicker supports most of the DatePicker props, read through DatePicker documentation to learn about all component features that are not listed on this page.

Use presets prop to add custom date presets. Presets are displayed next to the calendar:

You can pass props down to the underlying TimePicker component with timePickerProps prop. Example of enabling dropdown and setting 12h format for time picker:

Use valueFormat prop to change dayjs format of value label:

DateTimePicker component supports Input and Input.Wrapper components features and all button element props. DateTimePicker documentation does not include all features supported by the component – see Input documentation to learn about all available features.

Set clearable prop to display clear button in the right section. Note that if you set rightSection prop, clear button will not be displayed.

By default, picker is rendered inside Popover. You can change that to Modal by setting dropdownType="modal":

If DateTimePicker is used without label prop, it will not be announced properly by screen reader:

Set aria-label to make the input accessible. In this case label will not be visible, but screen reader will announce it:

If label prop is set, input will be accessible it is not required to set aria-label:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { DateTimePicker } from '@mantine/dates';

function Demo() {
  return <DateTimePicker label="Pick date and time" placeholder="Pick date and time" />;
}
```

```python
import { DateTimePicker } from '@mantine/dates';

function Demo() {
  return <DateTimePicker withSeconds label="Pick date and time" placeholder="Pick date and time" />;
}
```

```python
import dayjs from 'dayjs';
import { DateTimePicker } from '@mantine/dates';

function Demo() {
  return (
    <DateTimePicker
      label="Pick date and time"
      placeholder="Pick date and time"
      presets={[
        { value: dayjs().subtract(1, 'day').format('YYYY-MM-DD HH:mm:ss'), label: 'Yesterday' },
        { value: dayjs().format('YYYY-MM-DD HH:mm:ss'), label: 'Today' },
        { value: dayjs().add(1, 'day').format('YYYY-MM-DD HH:mm:ss'), label: 'Tomorrow' },
        { value: dayjs(
...
```

---

## Default props | Mantine

**URL**: https://mantine.dev/theming/default-props/

**Contents**:
- Default props
- Default props with MantineThemeProvider
- Default props for compound components
- useProps hook
- withProps function

You can define default props for every Mantine component by setting theme.components. These props will be used by default by all components of your application unless they are overridden by component props:

You can also use MantineThemeProvider to define default props for a part of your application:

Some components like Menu and Tabs have associated compound components: Menu.Item, Tabs.List, etc.. You can add default props to these components by omitting the dot from component name:

You can use useProps hook to add default props support to any custom component. useProps accepts three arguments:

All Mantine components have withProps static function that can be used to add default props to the component:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { MantineProvider, Button, Group, createTheme } from '@mantine/core';

const theme = createTheme({
  components: {
    Button: Button.extend({
      defaultProps: {
        color: 'cyan',
        variant: 'outline',
      },
    }),
  },
});

function Demo() {
  return (
    <MantineProvider theme={theme}>
      <Group>
        <Button>Default button</Button>
        <Button color="red" variant="filled">
          Button with props
        </Button>
      </Group>
    </MantineProvider>
 
...
```

```python
import {
  Button,
  createTheme,
  MantineThemeProvider,
} from '@mantine/core';

const theme = createTheme({
  components: {
    Button: Button.extend({
      defaultProps: {
        color: 'cyan',
        variant: 'outline',
      },
    }),
  },
});

function Demo() {
  return (
    <>
      <MantineThemeProvider theme={theme}>
        {/* Part of the app with theme */}
      </MantineThemeProvider>

      {/* Another part without theme */}
    </>
  );
}
```

```python
import {
  createTheme,
  MantineProvider,
  Menu,
  Tabs,
} from '@mantine/core';

const theme = createTheme({
  components: {
    MenuItem: Menu.Item.extend({
      defaultProps: { color: 'red' },
    }),

    TabsList: Tabs.List.extend({
      defaultProps: {
        justify: 'center',
      },
    }),
  },
});

function Demo() {
  return (
    <MantineProvider theme={theme}>
      {/* Your app here */}
    </MantineProvider>
  );
}
```

---

## Icons libraries | Mantine

**URL**: https://mantine.dev/guides/icons/

**Contents**:
- Icons libraries with Mantine
- Tabler icons
- Icons size
- Custom icons

You can use any icons library with Mantine components, most popular options are:

Tabler icons are used in Mantine demos, documentation and some @mantine/ packages depend on them. If you do not know which icons library to use, we recommend Tabler icons.

Most of the icons libraries support size prop (or similar width and height props) which allows changing icon width and height. Usually, it is a number in pixels.

rem units in size prop

Icons size prop is usually converted to width and height props under the hood. If you set size={16} it will be converted to width="16" and height="16" attributes on svg element.

You can use rem units in size prop: size="1rem" will be converted to width="1rem" and height="1rem", but it is not recommended as it is prohibited by SVG standard – some browsers (Firefox) will show a warning in the console.

It is recommended to use icons as React components. In this case, you will be able to use currentColor in the fill and stroke prop. This will change icon color based on the context it is used in.

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { IconBrandMantine } from '@tabler/icons-react';

function Demo() {
  return (
    <IconBrandMantine
      size={80}
      stroke={1.5}
      color="var(--mantine-color-blue-filled)"
    />
  );
}
```

```javascript
interface AddressBookIconProps extends React.ComponentPropsWithoutRef<'svg'> {
  size?: number | string;
}

export function AddressBookIcon({ size, style, ...others }: AddressBookIconProps) {
  return (
    <svg
      xmlns="http://www.w3.org/2000/svg"
      fill="none"
      stroke="currentColor"
      strokeLinecap="round"
      strokeLinejoin="round"
      strokeWidth="1.5"
      viewBox="0 0 24 24"
      style={{ width: size, height: size, ...style }}
      {...others}
    >
      <path stro
...
```

---

## MantineProvider | Mantine

**URL**: https://mantine.dev/theming/mantine-provider/

**Contents**:
- MantineProvider
- Usage
- MantineProvider props
  - theme
  - colorSchemeManager
  - defaultColorScheme
  - cssVariablesSelector
  - withCssVariables

MantineProvider provides a theme object context value, manages color scheme changes and injects CSS variables. It must be rendered at the root of your application and should be used only once.

MantineProvider supports the following props:

Pass theme object override to theme prop. It will be merged with the default theme and used in all components.

colorSchemeManager is used to retrieve and set color scheme value in external storage. By default, MantineProvider uses window.localStorage to store color scheme value, but you can pass your own implementation to colorSchemeManager prop. You can learn more about color scheme management in the color schemes guide.

defaultColorScheme value is used when colorSchemeManager cannot retrieve the value from external storage, for example during server side rendering or when the user hasn't selected a preferred color scheme. Possible values are light, dark and auto. By default, color scheme value is light. You can learn more about color scheme management in the color schemes guide.

cssVariablesSelector is a CSS selector to which CSS variables should be added. By default, it is :root. MantineProvider generates CSS variables based on given theme override and cssVariablesResolver, then these variables are rendered into <style /> tag next to your application. You can learn more about Mantine CSS variables in the CSS variables guide.

withCssVariables determines whether theme CSS variables should be added to given cssVariablesSelector. By default, it is set to true, you should not change it unless you want to manage CSS variables via .css file (Note that in this case you will need to generate all theme tokens that are not a part of the default theme on your side).

deduplicateCssVariables determines whether CSS variables should be deduplicated: if CSS variable has the same value as in default theme, it is not added in the runtime. By default, it is set to true. If set to false, all Mantine CSS variables will be added in <style /> ta

*[Content truncated - see full docs]*

**Examples**:

```python
import { createTheme, MantineProvider } from '@mantine/core';

const theme = createTheme({
  /** Your theme override here */
});

function Demo() {
  return (
    <MantineProvider theme={theme}>
      {/* Your app here */}
    </MantineProvider>
  );
}
```

```javascript
interface MantineProviderProps {
  /** Theme override object */
  theme?: MantineThemeOverride;

  /** Used to retrieve/set color scheme value in external storage, by default uses `window.localStorage` */
  colorSchemeManager?: MantineColorSchemeManager;

  /** Default color scheme value used when `colorSchemeManager` cannot retrieve value from external storage, `light` by default */
  defaultColorScheme?: MantineColorScheme;

  /** Forces color scheme value, if set, MantineProvider ignores `col
...
```

```python
import { createTheme, MantineProvider } from '@mantine/core';

const theme = createTheme({
  fontFamily: 'Open Sans, sans-serif',
  primaryColor: 'cyan',
});

function Demo() {
  return (
    <MantineProvider theme={theme}>
      {/* Your app here */}
    </MantineProvider>
  );
}
```

---

## Mantine

**URL**: https://mantine.dev/colors-generator/

**Contents**:
- Mantine colors generator

**Examples**:

```text
[
  "#ecf4ff",
  "#dce4f5",
  "#b9c7e2",
  "#94a8d0",
  "#748dc0",
  "#5f7cb7",
  "#5474b4",
  "#44639f",
  "#3a5890",
  "#2c4b80"
]
```

```python
import { MantineProvider, createTheme, MantineColorsTuple } from '@mantine/core';

const myColor: MantineColorsTuple = [
  '#ecf4ff',
  '#dce4f5',
  '#b9c7e2',
  '#94a8d0',
  '#748dc0',
  '#5f7cb7',
  '#5474b4',
  '#44639f',
  '#3a5890',
  '#2c4b80'
];

const theme = createTheme({
  colors: {
    myColor,
  }
});

function Demo() {
  return (
    <MantineProvider theme={theme}>
      {/* Your app here */}
    </MantineProvider>
  );
}
```

---

## Mantine

**URL**: https://mantine.dev/

I am a senior Frontend Developer and wanted to use something new instead of Material UI and came across this, it has been well thought of all the different scenarios you and come across, and the hooks are just pure love :)

Thank you so much for this.

---

## Migration guide Tiptap 2 → Tiptap 3 | Mantine

**URL**: https://mantine.dev/guides/tiptap-3-migration/

**Contents**:
- Migration guide Tiptap 2 → Tiptap 3
- shouldRerenderOnTransaction
- immediatelyRender
- StarterKit changes
- Import paths

This guide will help you update TipTap from version 2 to version 3.

Set shouldRerenderOnTransaction: true in useEditor. It is required to have active control highlight.

Set immediatelyRender: false if you use Next.js or other framework with server-side rendering. It is required to prevent hydration mismatches.

StarterKit now includes underline and link extensions out of the box:

Change import paths for floating and bubble menu components:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```javascript
const editor = useEditor({
  shouldRerenderOnTransaction: true,
  // ... other options
});
```

```javascript
const editor = useEditor({
  immediatelyRender: false,
  // ... other options
});
```

```python
// With tiptap 2.x – ❌ no longer works with tiptap 3.x
import Underline from '@tiptap/extension-underline';
import StarterKit from '@tiptap/starter-kit';
import { Link } from '@mantine/tiptap';

const editor = useEditor({
  extensions: [StarterKit, Underline, Link],
});

// With tiptap 3x – ✅ new usage example
import StarterKit from '@tiptap/starter-kit';
import { Link } from '@mantine/tiptap';

const editor = useEditor({
  // Remove underline and link extensions
  extensions: [StarterKit.config
...
```

---

## MiniCalendar | Mantine

**URL**: https://mantine.dev/dates/mini-calendar/

**Contents**:
- MiniCalendar
- Usage
- Number of days
- getDayProps
- Min and max dates
- Localization
- Accessibility

Compact calendar to display a small number of days in a row

Use numberOfDays prop to control how many days are displayed at once. The default value is 7.

Use getDayProps to add custom props to days, for example, assign styles to weekends:

Use minDate and maxDate props to limit date selection:

You can change localization both on component level with locale prop and globally with DatesProvider.

Use nextControlProps and previousControlProps to add aria-label and other props to navigation buttons:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { useState } from 'react';
import { MiniCalendar } from '@mantine/dates';

function Demo() {
  const [value, onChange] = useState<string | null>('2025-04-15');
  return <MiniCalendar value={value} onChange={onChange} numberOfDays={6} />;
}
```

```python
import { MiniCalendar } from '@mantine/dates';

function Demo() {
  return <MiniCalendar numberOfDays={5} />;
}
```

```python
import dayjs from 'dayjs';
import { MiniCalendar } from '@mantine/dates';

function Demo() {
  return (
    <MiniCalendar
      numberOfDays={6}
      getDayProps={(date) => ({
        style: {
          color: [0, 6].includes(dayjs(date).day()) ? 'var(--mantine-color-red-8)' : undefined,
        },
      })}
    />
  );
}
```

---

## Notifications system | Mantine

**URL**: https://mantine.dev/x/notifications/

**Contents**:
- Notifications system
- Installation
- Do not forget to import styles
- Functions
- Notification props
- Customize notification styles
- Notifications container position
- Limit and queue

Mantine notifications system

After installation import package styles at the root of your application:

Add Notifications component anywhere in your application. Note that:

All set! You can now use all notifications system features.

Followed installation instructions above but something is not working (position prop not working, notifications are stuck at the bottom)? You've fallen into the trap of not importing notifications styles! To fix the issue, import notifications styles at the root of your application:

@mantine/notifications package exports notifications object with the following functions:

All functions can be imported from @mantine/notifications package and can be used in any part of your application:

You can also import these functions separately:

notifications.show and notification.update functions can be called with an object that has the following properties:

All properties except message are optional.

Notifications preview (message prop used as children):

You can use style, className or Styles API classNames, styles props to customize notification styles. Usually, it is better to override Notification styles with classNames prop in the theme object.

You can define notification position in notifications.show function. Possible position values:

The position can be defined on the Notifications component. In the following example, notifications will be displayed in the top right corner of the screen if position is not defined in notifications.show function:

You can limit maximum number of notifications that are displayed at a time by setting limit prop on Notifications:

All notifications added after the limit was reached are added to the queue and displayed when notification from current state is hidden.

To remove specific notification from state or queue use notifications.hide function:

Use notifications.cleanQueue function to remove all notifications from the queue and notifications.clean to remove all notifications both from the state 

*[Content truncated - see full docs]*

**Examples**:

```text
yarn add @mantine/notifications
```

```text
npm install @mantine/notifications
```

```text
import '@mantine/core/styles.css';
// ‼️ import notifications styles after core package styles
import '@mantine/notifications/styles.css';
```

---

## Spotlight | Mantine

**URL**: https://mantine.dev/x/spotlight/

**Contents**:
- Spotlight
- Installation
- Usage
- Actions
- Spotlight store
- Keyboard shortcuts
- Limit prop
- Scrollable actions list

Command center for your application

After installation import package styles at the root of your application:

Spotlight component can be used as a search or as a command center of your application. It is used as a search on mantine.dev website, you can trigger it with Ctrl + K shortcut. Spotlight is based on Modal component and supports most of its props.

@mantine/spotlight package exports an object with actions that can be used to control the spotlight:

These actions can be passed to event listeners or used anywhere in your application (not limited to React components):

You can also import actions directly from the @mantine/spotlight package, if you prefer this syntax:

spotlight object documented above uses the default store, it works fine if you have only one spotlight in your application. In case you need multiple spotlights, you need to create your own store for each of them:

Spotlight uses use-hotkeys hook to handle keyboard shortcuts. By default, Ctrl + K and Cmd + K shortcuts are used to open spotlight, you can change them with shortcut prop:

Use limit prop to limit the maximum number of actions that can be displayed at a time. Usually, 5–7 actions is a good number. limit prop is crucial for performance in case you have a lot of actions, it will prevent the spotlight from rendering all of them at once.

The example below renders 3000 actions, but only 7 of them are displayed at a time:

By default, Spotlight actions list is not scrollable. If you have a lot of actions that you need to display at a time, set scrollable and maxHeight props. Note that there are caveats with both approaches:

In other words, if you want the actions list to shrink, do not set scrollable prop and use limit prop. If you want the actions list to always have a fixed height, set scrollable and maxHeight props.

Spotlight supports actions groups, you can use them to group actions by category:

If you need more control over spotlight rendering and logic, use compound components. 

*[Content truncated - see full docs]*

**Examples**:

```text
yarn add @mantine/spotlight
```

```text
npm install @mantine/spotlight
```

```text
import '@mantine/core/styles.css';
// ‼️ import spotlight styles after core package styles
import '@mantine/spotlight/styles.css';
```

---

## Support | Mantine

**URL**: https://mantine.dev/support/

**Contents**:
- Support
- Get help
- Report an issue
- Get help on GitHub Discussions
- Support Mantine

This guide will help you understand how to get help, report bugs and connect with the community. Keep in mind that Mantine is maintained by a small team of developers, all Mantine projects are open-source and free for everyone.

If you have any questions, need help with Mantine, want to request a feature, or just want to chat with other developers, you can:

We use GitHub issues to track bugs. You can find a list of current open issues on this page. Usually, it takes up to 3 weeks to review and fix the issue. Issues reported on GitHub are fixed only in patch releases (8.0.x) – minor and major releases are reserved for new features and breaking changes.

If you found a bug and want to report it, please follow these steps:

GitHub discussion are used for questions, feature requests, feedback, showcase and discussions. If clearly stated, questions are usually answered within 24 hours. To get help on GitHub Discussions:

All contributions to the projects are welcome and appreciated. There are many ways to support the project:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

---

## Testing with Jest | Mantine

**URL**: https://mantine.dev/guides/jest/

**Contents**:
- Testing with Jest
- Custom render
- Mock WEB APIs
- Framework specific setup
- Testing examples

This guide will help you setup Jest and React Testing Library for your project. Note that this guide only covers shared logic that can be applied to any framework, and it does not cover initial setup of Jest and React Testing Library as it may vary depending on the framework you are using.

All Mantine components require MantineProvider to be present in the component tree. To add MantineProvider to the component tree in your tests, create a custom render function:

It is usually more convenient to export all @testing-library/* functions that you are planning to use from ./testing-utils/index.ts file:

Then you should import all testing utilities from ./testing-utils instead of @testing-library/react:

Most of Mantine components depend on browser APIs like window.matchMedia or ResizeObserver. These APIs are not available in jest-environment-jsdom environment and you will need to mock them in your tests.

Create jest.setup.js file in your project root and add the following code to it:

Then add it as a setup file in your jest.config.js:

Jest setup for different frameworks may vary and usually change over time. To learn how to setup Jest for your framework, either check Jest and React Testing Library documentation or check one of the premade templates. Most of the templates include Jest setup, and you can use them as a reference.

You can find testing examples in Mantine Help Center:

Usage with JavaScript

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
// ./test-utils/render.tsx
import { render as testingLibraryRender } from '@testing-library/react';
import { MantineProvider } from '@mantine/core';
// Import your theme object
import { theme } from '../src/theme';

export function render(ui: React.ReactNode) {
  return testingLibraryRender(<>{ui}</>, {
    wrapper: ({ children }: { children: React.ReactNode }) => (
      <MantineProvider theme={theme} env="test">{children}</MantineProvider>
    ),
  });
}
```

```python
import userEvent from '@testing-library/user-event';

export * from '@testing-library/react';
export { render } from './render';
export { userEvent };
```

```python
import { render, screen } from '../test-utils';
import { Welcome } from './Welcome';

describe('Welcome component', () => {
  it('has correct Next.js theming section link', () => {
    render(<Welcome />);
    expect(screen.getByText('this guide')).toHaveAttribute(
      'href',
      'https://mantine.dev/guides/next/'
    );
  });
});
```

---

## Testing with Vitest | Mantine

**URL**: https://mantine.dev/guides/vitest/

**Contents**:
- Testing with Vitest
- Installation
- Configuration
- Custom render
- Example of a full setup

This guide will help you setup Vitest and React Testing Library for your project. Note that this guide intended for projects that use Vite as a bundler, if you are using other frameworks/bundlers, it is recommended to use Jest instead.

Install vitest and react testing library:

If you want to run tests from your IDE, install one of the extensions.

Add vitest configuration to your Vite config file:

Then create vitest.setup.mjs file in your project root and add the following code to it:

The code above mocks window.matchMedia and ResizeObserver APIs that are not available in jsdom environment but are required by some Mantine components.

Optionally you can add vitest scripts to your package.json:

All Mantine components require MantineProvider to be present in the component tree. To add MantineProvider to the component tree in your tests, create a custom render function:

It is usually more convenient to export all @testing-library/* functions that you are planning to use from ./testing-utils/index.ts file:

Then you should import all testing utilities from ./testing-utils instead of @testing-library/react:

You can find an example with a full Vitest setup in mantine-vite-template.

eslint-config-mantine

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```text
yarn add --dev vitest jsdom @testing-library/dom @testing-library/jest-dom @testing-library/react @testing-library/user-event
```

```text
npm install --save-dev vitest jsdom @testing-library/dom @testing-library/jest-dom @testing-library/react @testing-library/user-event
```

```python
import { defineConfig } from 'vite';

export default defineConfig({
  // ... rest of your config
  test: {
    globals: true,
    environment: 'jsdom',
    setupFiles: './vitest.setup.mjs',
  },
});
```

---

## TimeInput | Mantine

**URL**: https://mantine.dev/dates/time-input/

**Contents**:
- TimeInput
- Usage
- TimePicker component
- Controlled
- Show browser picker
- With seconds
- With icon
- Disabled state

Capture time from the user

TimeInput component supports Input and Input.Wrapper components features and all input element props. TimeInput documentation does not include all features supported by the component – see Input documentation to learn about all available features.

TimeInput component is based on the native input[type="time"] element and does not support most of advanced features like choosing time format or custom dropdown with time select. If you need more features, use TimePicker component instead.

TimeInput features/limitations:

You can show browser picker by calling showPicker method of input element. Note that some browsers (desktop Safari) do not support this feature and the method will do nothing.

If TimeInput is used without label prop, it will not be announced properly by screen reader:

Set aria-label to make the input accessible. In this case label will not be visible, but screen reader will announce it:

If label prop is set, input will be accessible it is not required to set aria-label:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { TimeInput } from '@mantine/dates';

function Demo() {
  return (
    <TimeInput
      label="Input label"
      description="Input description"
    />
  );
}
```

```python
import { useState } from 'react';
import { TimeInput } from '@mantine/dates';

function Demo() {
  const [value, setValue] = useState('');
  return (
    <TimeInput
      value={value}
      onChange={(event) => setValue(event.currentTarget.value)}
    />
  );
}
```

```python
import { useRef } from 'react';
import { ActionIcon } from '@mantine/core';
import { TimeInput } from '@mantine/dates';
import { IconClock } from '@tabler/icons-react';

function Demo() {
  const ref = useRef<HTMLInputElement>(null);

  const pickerControl = (
    <ActionIcon variant="subtle" color="gray" onClick={() => ref.current?.showPicker()}>
      <IconClock size={16} stroke={1.5} />
    </ActionIcon>
  );

  return (
    <TimeInput label="Click icon to show browser picker" ref={ref} right
...
```

---

## TimePicker | Mantine

**URL**: https://mantine.dev/dates/time-picker/

**Contents**:
- TimePicker
- Usage
- Controlled
- With seconds
- 12-hour format
- Change am/pm labels
- Min and max values
- With dropdown

Captures time value from the user

TimePicker component is an alternative to TimeInput that offers more features, it supports 24-hour and 12-hour formats, dropdown with hours, minutes and seconds, and more.

TimePicker component value is a string in hh:mm:ss 24-hour format (for example 18:34:55). Empty string is used to represent no value. onChange function is called only when the entered value is valid. The input value is considered valid in the following cases:

Set withSeconds prop to enable seconds input. Note that if this prop is used, onChange is not called until all inputs are filled – it is not possible to enter only hours and minutes.

Set format="12h" to use 12-hour format. Note that onChange is called only when all inputs are filled including am/pm input.

To change am/pm labels use amPmLabels prop. Example of changing labels to Hindi:

Set min and max props to limit available time range:

Set withDropdown prop to display the dropdown with hours, minutes, seconds and am/pm selects. By default, the dropdown is visible when one of the inputs is focused.

Use hoursStep, minutesStep and secondsStep props to control step for each input. These props are used to control value by which the input is incremented or decremented when up/down arrow keys are pressed and to generate corresponding values range in the dropdown.

Use popoverProps to pass props down to the underlying Popover component:

You can define time presets with presets prop. Presets are displayed in the dropdown and can be selected by clicking on them. Time values for presets should be in hh:mm:ss or hh:mm 24-hour time format. Presets display value is generated based on format, amPmLabels and withSeconds props.

To group presets use an array of objects with label and values keys:

If you need to generate a range of time values, use getTimeRange function exported from @mantine/dates package. The function accepts start, end time and interval in hh:mm:ss format.

By default, the dropdown is displayed b

*[Content truncated - see full docs]*

**Examples**:

```python
import { TimePicker } from '@mantine/dates';

function Demo() {
  return <TimePicker label="Enter time" />;
}
```

```python
import { useState } from 'react';
import { TimePicker } from '@mantine/dates';

function Demo() {
  const [value, setValue] = useState('');
  return <TimePicker value={value} onChange={setValue} />;
}
```

```python
import { TimePicker } from '@mantine/dates';

function Demo() {
  return <TimePicker label="Enter time" withSeconds />;
}
```

---

## Usage with Gatsby | Mantine

**URL**: https://mantine.dev/guides/gatsby/

**Contents**:
- Usage with Gatsby
- Get started with a template
- Generate new application
- Installation
- PostCSS setup
- Setup
- CSS modules

The easiest way to get started is to use one of the templates. All templates are configured correctly: they include PostCSS setup, ColorSchemeScript and other essential features. Some templates also include additional features like Jest, Storybook and ESLint.

If you are not familiar with GitHub, you can find a detailed instruction on how to bootstrap a project from a template on this page.

Gatsby template with basic setup

Follow Gatsby quick start guide to create new Gatsby application:

When asked "Would you like to install a styling system?", select PostCSS.

Choose packages that you will use in your application:

Hooks for state and UI management

Core components library: inputs, buttons, overlays, etc.

Form management library

Date inputs, calendars

Recharts based charts library

Code highlight with your theme colors and styles

Rich text editor based on Tiptap

Capture files with drag and drop

Embla based carousel component

Overlay command center

Centralized modals manager

Install dependencies:

Install PostCSS plugins and postcss-preset-mantine:

Create postcss.config.cjs file at the root of your application with the following content:

Create src/theme.ts file with your theme override:

Create gatsby-ssr.tsx with the following content:

Create gatsby-browser.tsx with the following content:

All set! Start development server:

By default, Gatsby has different syntax for importing CSS modules:

Usage with React Router

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```text
yarn create gatsby
```

```text
npm init gatsby
```

```text
yarn add @mantine/core @mantine/hooks
```

---

## Usage with JavaScript | Mantine

**URL**: https://mantine.dev/guides/javascript/

**Contents**:
- Usage with JavaScript
- Is it possible to use Mantine with JavaScript?
- Transforming demos code to JavaScript
- Should Mantine be used with JavaScript?

Yes, it is possible to use all @mantine/* packages (as well as all other npm packages) with JavaScript. @mantine/* packages are written in TypeScript and have type definitions, so you will get some the benefits of TypeScript (like autocompletion in your IDE) when using them with JavaScript.

All demos in Mantine documentation are written in TypeScript. In most cases there is no difference between TypeScript and JavaScript code – you do not have to do anything.

To transform TypeScript code to JavaScript you can use TypeScript playground – paste demo code into the playground and all types will be removed. Note that you will also need to remove type imports from the code.

Example of transformed code:

It is recommended to use Mantine with TypeScript, it does not require deep knowledge of TypeScript and will make your code more robust and easier to maintain. For example, you will get type errors when you pass invalid props to components or when you use non-existing props. TypeScript will also help you during migration to new versions of Mantine – you will get type errors when props/components that you have in your code are removed/renamed/changed.

If you are not familiar with TypeScript yet, using Mantine with TypeScript will be a great opportunity to learn it. You can use any of templates to get started – all of them include TypeScript support out of the box.

Usage with TypeScript

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
// TypeScript code
import { Button, ButtonProps } from '@mantine/core';

interface MyButtonProps extends ButtonProps {
  myProp: string;
}

function MyButton({ myProp, ...others }: MyButtonProps) {
  return <Button {...others} />;
}
```

```python
// JavaScript code
import { Button } from '@mantine/core';

function MyButton({ myProp, ...others }) {
  return <Button {...others} />;
}
```

---

## Usage with Next.js | Mantine

**URL**: https://mantine.dev/guides/next/

**Contents**:
- Usage with Next.js
- Get started with a template
- Generate new application
- Installation
- PostCSS setup
- Setup with pages router
- Setup with app router
- app + pages router together

The easiest way to get started is to use one of the templates. All templates are configured correctly: they include PostCSS setup, ColorSchemeScript and other essential features. Some templates also include additional features like Jest, Storybook and ESLint.

If you are not familiar with GitHub, you can find a detailed instruction on how to bootstrap a project from a template on this page.

Next.js template with app router and full setup: Jest, Storybook, ESLint

Next.js template with pages router and full setup: Jest, Storybook, ESLint

next-app-min-template

Next.js template with app router and minimal setup – no additional tools included, only default Next.js configuration

next-pages-min-template

Next.js template with pages router and minimal setup – no additional tools included, only default Next.js configuration

next-vanilla-extract-template

Next.js template with Vanilla extract example

Follow create-next-app guide to create new Next.js application:

Choose packages that you will use in your application:

Hooks for state and UI management

Core components library: inputs, buttons, overlays, etc.

Form management library

Date inputs, calendars

Recharts based charts library

Code highlight with your theme colors and styles

Rich text editor based on Tiptap

Capture files with drag and drop

Embla based carousel component

Overlay command center

Centralized modals manager

Install dependencies:

Install PostCSS plugins and postcss-preset-mantine:

Create postcss.config.cjs file at the root of your application with the following content:

Add styles imports and MantineProvider to the pages/_app.tsx file:

Create pages/_document.tsx file with ColorSchemeScript component. Note that it is required even if you use only one color scheme in your application.

All set! Start development server:

Add MantineProvider, ColorSchemeScript and styles imports to the app/layout.tsx file:

All set! Start development server:

If you use both app and pages router in one app

*[Content truncated - see full docs]*

**Examples**:

```text
yarn create next-app --typescript
```

```text
npx create-next-app@latest --typescript
```

```text
yarn add @mantine/core @mantine/hooks
```

---

## Usage with Redwood | Mantine

**URL**: https://mantine.dev/guides/redwood/

**Contents**:
- Usage with RedwoodJS
- Get started with a template
- Generate new application
- Installation
- PostCSS setup
- Setup

The easiest way to get started is to use one of the templates. All templates are configured correctly: they include PostCSS setup, ColorSchemeScript and other essential features. Some templates also include additional features like Jest, Storybook and ESLint.

If you are not familiar with GitHub, you can find a detailed instruction on how to bootstrap a project from a template on this page.

RedwoodJS template with basic setup

Follow Redwood getting started guide guide to create new Redwood application:

Note that it is recommended to use yarn instead of npm to install dependencies.

Open web directory before installing dependencies:

Choose packages that you will use in your application:

Hooks for state and UI management

Core components library: inputs, buttons, overlays, etc.

Form management library

Date inputs, calendars

Recharts based charts library

Code highlight with your theme colors and styles

Rich text editor based on Tiptap

Capture files with drag and drop

Embla based carousel component

Overlay command center

Centralized modals manager

Install dependencies:

Install PostCSS plugins and postcss-preset-mantine:

Create postcss.config.js file in web directory with the following content:

Add styles imports, MantineProvider and ColorSchemeScript to web/src/App.tsx file:

All set! Start development server:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```text
yarn create redwood-app my-redwood-project --typescript
```

```text
yarn add @mantine/core @mantine/hooks
```

```text
npm install @mantine/core @mantine/hooks
```

---

## Usage with Storybook | Mantine

**URL**: https://mantine.dev/guides/storybook/

**Contents**:
- Setup Mantine in Storybook
- Add Storybook to your application
- Configure addons
- Theme object
- Storybook preview

Note that this guide covers only Storybook 7.0+ integration. If you are using older version of Storybook, it will not work for you.

If you already have Storybook in your application, you can skip this step.

Follow Storybook getting started guide to add Storybook to your application:

Note that @storybook/addon-styling-webpack is required only if you are not using Vite. If you are using Vite, do not install @storybook/addon-styling-webpack and do not add it to the addons section in main.ts file.

Install Storybook addons:

Add addons to .storybook/main.ts:

To shared theme object between your application and Storybook, create src/theme.ts (or any other path in your application) file with your theme override:

Then you will be able to use the same theme both in your application and Storybook:

If .storybook/preview.tsx file does not exist, create it and add the following content:

All set! Start Storybook:

Usage with TypeScript

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```text
npx storybook@latest init
```

```text
yarn add --dev storybook-dark-mode @storybook/addon-styling-webpack
```

```text
npm install --save-dev storybook-dark-mode @storybook/addon-styling-webpack
```

---

## Usage with Vite | Mantine

**URL**: https://mantine.dev/guides/vite/

**Contents**:
- Usage with Vite
- Get started with a template
- Generate new application
- Installation
- PostCSS setup
- Setup

The easiest way to get started is to use one of the templates. All templates are configured correctly: they include PostCSS setup, ColorSchemeScript and other essential features. Some templates also include additional features like Jest, Storybook and ESLint.

If you are not familiar with GitHub, you can find a detailed instruction on how to bootstrap a project from a template on this page.

Vite template with full setup: Vitest, Prettier, Storybook, ESLint

Vite template with minimal setup – no additional tools included, only default Vite configuration

vite-vanilla-extract-template

Vite template with Vanilla extract example

Follow Vite getting started guide to create new Vite application:

Choose packages that you will use in your application:

Hooks for state and UI management

Core components library: inputs, buttons, overlays, etc.

Form management library

Date inputs, calendars

Recharts based charts library

Code highlight with your theme colors and styles

Rich text editor based on Tiptap

Capture files with drag and drop

Embla based carousel component

Overlay command center

Centralized modals manager

Install dependencies:

Install PostCSS plugins and postcss-preset-mantine:

Create postcss.config.cjs file at the root of your application with the following content:

Add styles imports and MantineProvider to your application root component (usually App.tsx):

All set! Start development server:

Usage with React Router

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```text
yarn create vite
```

```text
npm create vite@latest
```

```text
yarn add @mantine/core @mantine/hooks
```

---

## eslint-config-mantine | Mantine

**URL**: https://mantine.dev/eslint-config-mantine/

**Contents**:
- Mantine ESLint config
- Installation
- Usage
- Rules and source code

eslint-config-mantine is a set of ESLint rules and configurations used in Mantine projects. You can use it in your project to ensure that your code follows the same style and conventions as Mantine.

Mantine ESLint config requires ESLint 9 or higher:

Add the following configuration to your eslint.config.mjs:

Mantine ESLint config extends recommended ESLint, typescript-eslint and eslint-plugin-jsx-a11y rules and adds custom rules and configurations. You can find the full list of rules and source code in the eslint-config-mantine repository.

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```text
yarn add --dev @eslint/js eslint eslint-plugin-jsx-a11y eslint-plugin-react typescript-eslint eslint-config-mantine
```

```text
npm install --save-dev @eslint/js eslint eslint-plugin-jsx-a11y eslint-plugin-react typescript-eslint eslint-config-mantine
```

```python
import mantine from 'eslint-config-mantine';
import tseslint from 'typescript-eslint';

export default tseslint.config(
  ...mantine,
  { ignores: ['**/*.{mjs,cjs,js,d.ts,d.mts}'] },
);
```

---
