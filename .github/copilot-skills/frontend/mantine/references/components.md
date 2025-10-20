# Mantine - Components

**Pages**: 87

---

## 7.x to 8.x migration | Mantine

**URL**: https://mantine.dev/guides/7x-to-8x/

**Contents**:
- 7.x → 8.x migration guide
- Global styles imports
- Portal reuseTargetNode
- Switch withThumbIndicator
- Date string values
- DatesProvider timezone
- DateTimePicker timeInputProps
- CodeHighlight usage

If you used separate styles imports from @mantine/core/styles/global.css , you need to update imports to use new files. Note that if you previously imported @mantine/core/styles.css, no changes are required – all new files are already included in styles.css.

If you used @mantine/core/styles.css, no changes are required, the import works the same in 7.x and 8.x versions:

reuseTargetNode prop of Portal component is now enabled by default. This option improves performance by reusing the target node between portal renders, but in some edge cases, it might cause issues with z-index stacking context.

If you experience issues with z-index, change reuseTargetNode prop to false in theme:

Switch component default styles were updated, it now includes checked state indicator inside the thumb. If you want to use old styles without indicator, set withThumbIndicator prop to false in theme:

@mantine/dates components now use date string values in onChange and other callbacks. If you want to continue using @mantine/dates components the same way as in 7.x, you need to convert callback values to Date objects:

DatesProvider component no longer supports timezone option:

If you need to handle timezones in your application, you can use a dedicated dates library (dayjs, luxon, date-fns) to update timezone values. Example of using Mantine components with dayjs:

DateTimePicker component no longer accepts timeInputProps prop, as the underlying TimeInput component was replaced with TimePicker. To pass props down to TimePicker component, use timePickerProps prop instead.

@mantine/code-highlight package no longer depends on highlight.js. You can follow the updated documentation to set up syntax highlighting with shiki.

If you want to continue using highlight.js, in your application, install highlight.js package:

Then wrap your app with CodeHighlightAdapterProvider and provide createHighlightJsAdapter as adapter prop:

Then you need to add styles of one of the highlight.js themes to you

*[Content truncated - see full docs]*

**Examples**:

```text
// ❌ No longer includes all global styles
import '@mantine/core/styles/global.css';
```

```text
// ✅ Import all global styles separately
import '@mantine/core/styles/baseline.css';
import '@mantine/core/styles/default-css-variables.css';
import '@mantine/core/styles/global.css';
```

```text
// 👍 No changes needed if you used styles.css
import '@mantine/core/styles.css';
```

---

## Accordion | Mantine

**URL**: https://mantine.dev/core/accordion/

**Contents**:
- Accordion
- Usage
- Change chevron
- Custom control label
- With icons
- Change transition
- Default opened items
- Control opened state

Divide content into collapsible sections

Accordion allows users to expand and collapse sections of content. It helps manage large amounts of information in a limited space by showing only the section headers initially and revealing content on interaction.

Accordion is commonly used for:

Use the chevron prop to change the chevron icon. When chevron is set, chevronIconSize prop is ignored. To remove the chevron icon, use chevron={null}.

To customize chevron styles, use Styles API with data-rotate attribute. It is set when the item is opened if the disableChevronRotation prop is not set.

Example of a custom chevron icon with rotation styles:

You can use any React node as a label for Accordion.Control component. When you use nested elements in Accordion.Control, it is recommended to set aria-label attribute to make the control accessible for screen readers.

Bender Bending Rodríguez

Fascinated with cooking, though has no sense of taste

Bender Bending Rodríguez, (born September 4, 2996), designated Bending Unit 22, and commonly known as Bender, is a bending unit created by a division of MomCorp in Tijuana, Mexico, and his serial number is 2716057. His mugshot id number is 01473. He is Fry's best friend.

One of the richest people on Earth

Carol Miller (born January 30, 2880), better known as Mom, is the evil chief executive officer and shareholder of 99.7% of Momcorp, one of the largest industrial conglomerates in the universe and the source of most of Earth's robots. She is also one of the main antagonists of the Futurama series.

Overweight, lazy, and often ignorant

Homer Jay Simpson (born May 12) is the main protagonist and one of the five main characters of The Simpsons series(or show). He is the spouse of Marge Simpson and father of Bart, Lisa and Maggie Simpson.

Use icon prop to display any element on the left section of the Accordion.Control:

To change transition duration, set transitionDuration prop:

To disable transitions, set transitionDuration to 

*[Content truncated - see full docs]*

**Examples**:

```python
import { Accordion } from '@mantine/core';
import { data } from './data';

function Demo() {
  const items = data.map((item) => (
    <Accordion.Item key={item.value} value={item.value}>
      <Accordion.Control icon={item.emoji}>{item.value}</Accordion.Control>
      <Accordion.Panel>{item.description}</Accordion.Panel>
    </Accordion.Item>
  ));

  return (
    <Accordion defaultValue="Apples">
      {items}
    </Accordion>
  );
}
```

```python
import { IconPlus } from '@tabler/icons-react';
import { Accordion } from '@mantine/core';
import { data } from './data';
import classes from './Demo.module.css';

function Demo() {
  const items = data.map((item) => (
    <Accordion.Item key={item.value} value={item.value}>
      <Accordion.Control icon={item.emoji}>{item.value}</Accordion.Control>
      <Accordion.Panel>{item.description}</Accordion.Panel>
    </Accordion.Item>
  ));

  return (
    <Accordion
      defaultValue="Apples"
     
...
```

```python
import { Group, Avatar, Text, Accordion } from '@mantine/core';

const charactersList = [
  {
    id: 'bender',
    image: 'https://img.icons8.com/clouds/256/000000/futurama-bender.png',
    label: 'Bender Bending Rodríguez',
    description: 'Fascinated with cooking, though has no sense of taste',
    content: "Bender Bending Rodríguez, (born September 4, 2996), designated Bending Unit 22, and commonly known as Bender, is a bending unit created by a division of MomCorp in Tijuana, Mexico, and h
...
```

---

## ActionIcon | Mantine

**URL**: https://mantine.dev/core/action-icon/

**Contents**:
- ActionIcon
- Usage
- Gradient variant
- Size
- Disabled state
- Disabled state when ActionIcon is link
- Customize disabled styles
- Disabled button with Tooltip

When variant prop is set to gradient, you can control gradient with gradient prop, it accepts an object with from, to and deg properties. If thegradient prop is not set, ActionIcon will use theme.defaultGradient which can be configured on the theme object. gradient prop is ignored when variant is not gradient.

Note that variant="gradient" supports only linear gradients with two colors. If you need a more complex gradient, then use Styles API to modify ActionIcon styles.

You can use any valid CSS value in size prop, it is used to set width, min-width, min-height and height properties. Note that size prop does not control child icon size, you need to set it manually on icon component. When size is a number, the value is treated as px units and converted to rem units.

If you want ActionIcon to have the same size as Mantine inputs, use size="input-sm" prop:

To make ActionIcon disabled set disabled prop, this will prevent any interactions with the button and add disabled styles. If you want the button to just look disabled but still be interactive, set data-disabled prop instead. Note that disabled styles are the same for all variants.

<a /> element does not support disabled attribute. To make ActionIcon disabled when it is rendered as a link, set data-disabled attribute instead and prevent default behavior in onClick event handler.

To customize disabled styles, it is recommended to use both &:disabled and &[data-disabled] selectors:

onMouseLeave event is not triggered when ActionIcon is disabled, so if you need to use Tooltip with disabled ActionIcon you need to set data-disabled prop on ActionIcon instead of disabled. Note that it is also required to change onClick event handler to (event) => event.preventDefault() as ActionIcon is not actually disabled and will still trigger onClick event.

When loading prop is set, ActionIcon will be disabled and Loader with overlay will be rendered in the center of the button. Loader color depends on ActionIcon variant.

You 

*[Content truncated - see full docs]*

**Examples**:

```python
import { ActionIcon } from '@mantine/core';
import { IconAdjustments } from '@tabler/icons-react';

function Demo() {
  return (
    <ActionIcon variant="filled" aria-label="Settings">
      <IconAdjustments style={{ width: '70%', height: '70%' }} stroke={1.5} />
    </ActionIcon>
  );
}
```

```python
import { ActionIcon } from '@mantine/core';
import { IconHeart } from '@tabler/icons-react';

function Demo() {
  return (
    <ActionIcon
      variant="gradient"
      size="xl"
      aria-label="Gradient action icon"
      gradient={{ from: 'blue', to: 'cyan', deg: 90 }}
    >
      <IconHeart />
    </ActionIcon>
  );
}
```

```python
import { ActionIcon } from '@mantine/core';
import { IconHeart } from '@tabler/icons-react';

function Demo() {
  return (
    <ActionIcon size={42} variant="default" aria-label="ActionIcon with size as a number">
      <IconHeart size={24} />
    </ActionIcon>
  );
}
```

---

## Alert | Mantine

**URL**: https://mantine.dev/core/alert/

**Contents**:
- Alert
- Usage
- Styles API
- Accessibility

Attract user attention with important static message

Alert supports Styles API, you can add styles to any inner element of the component withclassNames prop. Follow Styles API documentation to learn more.

Hover over selectors to highlight corresponding elements

Wrapper around `body` and `icon`

Body element, contains `title` and `message`

Title element, contains `label` and `icon`

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { Alert } from '@mantine/core';
import { IconInfoCircle } from '@tabler/icons-react';

function Demo() {
  const icon = <IconInfoCircle />;
  return (
    <Alert variant="light" color="blue" title="Alert title" icon={icon}>
      Lorem ipsum dolor sit, amet consectetur adipisicing elit. At officiis, quae tempore necessitatibus placeat saepe.
    </Alert>
  );
}
```

```text
/*
 * Hover over selectors to apply outline styles
 *
 */
```

```python
import { Alert } from '@mantine/core';

function Invalid() {
  // -> not ok
  return <Alert withCloseButton />;
}

function Valid() {
  // -> ok
  return <Alert withCloseButton closeButtonLabel="Dismiss" />;
}

function AlsoValid() {
  // -> ok, without close button, closeButtonLabel is not needed
  return <Alert />;
}
```

---

## AngleSlider | Mantine

**URL**: https://mantine.dev/core/angle-slider/

**Contents**:
- AngleSlider
- Usage
- Controlled
- formatLabel
- Marks
- onChangeEnd
- disabled
- Accessibility

Pick angle value between 0 and 360

Use AngleSlider component to pick angle value between 0 and 360:

AngleSlider value is a number between 0 and 360.

Use the formatLabel prop to change the angle label format. It accepts a function that takes the angle value and returns a React node:

Set the marks prop to display marks on the slider. Mark is an object of value (required, number between 0 and 360) and label (optional, React node). To restrict selection to marks only, set the restrictToMarks prop:

The onChangeEnd callback fires when the user stops dragging the slider or changes its value with the keyboard. Use it as a debounced callback to prevent frequent updates.

disabled prop disables the component and prevents user interaction:

To make the component accessible for screen readers, set the aria-label prop:

Keyboard interactions when the component is focused:

AngleSlider is based on the use-radial-move hook. You can build a custom radial slider using this hook if you need more control over the component's behavior.

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { AngleSlider } from '@mantine/core';

function Demo() {
  return <AngleSlider aria-label="Angle slider" size={60} thumbSize={8} />;
}
```

```python
import { useState } from 'react';
import { AngleSlider } from '@mantine/core';

function Demo() {
  const [value, setValue] = useState(180);
  return <AngleSlider value={value} onChange={setValue} />;
}
```

```python
import { AngleSlider } from '@mantine/core';

function Demo() {
  return <AngleSlider aria-label="Angle slider" formatLabel={(value) => `${value}°`} />;
}
```

---

## Autocomplete | Mantine

**URL**: https://mantine.dev/core/autocomplete/

**Contents**:
- Autocomplete
- Made with Combobox
- Not a searchable select
- Usage
- Controlled
- Select first option on change
- autoSelectOnBlur
- Data formats

Autocomplete user input with any list of options

Autocomplete is an opinionated component built on top of Combobox component. It has a limited set of features to cover only the basic use cases. If you need more advanced features, you can build your own component with Combobox. You can find examples of custom autocomplete components on the examples page.

Autocomplete is not a searchable select, it is a text input with suggestions. Values are not enforced to be one of the suggestions, user can type anything. If you need a searchable select, use Select component instead. To learn more about the differences between Autocomplete and Select, check help center article.

Autocomplete provides user a list of suggestions based on the input, however user is not limited to suggestions and can type anything.

Autocomplete value must be a string, other types are not supported. onChange function is called with a string value as a single argument.

Set the selectFirstOptionOnChange prop to automatically select the first option in the dropdown when the input value changes. This feature allows users to type a value and immediately press Enter to select the first matching option, without needing to press the arrow down key first.

Set autoSelectOnBlur prop to automatically select the highlighted option when the input loses focus. To see this feature in action: select an option with up/down arrows, then click outside the input:

Autocomplete data prop accepts data in one of the following formats:

Array of groups with string options:

Example of a custom filter function that matches options by words instead of letters sequence:

By default, options are sorted by their position in the data array. You can change this behavior with filter function:

The best strategy for large data sets is to limit the number of options that are rendered at the same time. You can do it with limit prop. Note that if you use a custom filter function, you need to implement your own logic to limit the numbe

*[Content truncated - see full docs]*

**Examples**:

```python
import { Autocomplete } from '@mantine/core';

function Demo() {
  return (
    <Autocomplete
      label="Your favorite library"
      placeholder="Pick value or enter anything"
      data={['React', 'Angular', 'Vue', 'Svelte']}
    />
  );
}
```

```python
import { useState } from 'react';
import { Autocomplete } from '@mantine/core';

function Demo() {
  const [value, setValue] = useState('');
  return <Autocomplete data={[]} value={value} onChange={setValue} />;
}
```

```python
import { Autocomplete } from '@mantine/core';

function Demo() {
  return (
    <Autocomplete
      label="Your favorite library"
      placeholder="Pick value or enter anything"
      selectFirstOptionOnChange
      data={['React', 'Angular', 'Vue', 'Svelte']}
    />
  );
}
```

---

## Avatar | Mantine

**URL**: https://mantine.dev/core/avatar/

**Contents**:
- Avatar
- Usage
- Initials
- Allowed initials colors
- Placeholder
- Variants
- Avatar.Group
- Polymorphic component

Display user profile image, initials or fallback icon

To display initials instead of the default placeholder, set name prop to the name of the person, for example, name="John Doe". If the name is set, you can use color="initials" to generate color based on the name:

By default, all colors from the default theme are allowed for initials, you can restrict them by providing allowedInitialsColors prop with an array of colors. Note that the default colors array does not include custom colors defined in the theme, you need to provide them manually if needed.

If the image cannot be loaded or not provided, Avatar will display a placeholder instead. By default, placeholder is an icon, but it can be changed to any React node:

Avatar.Group component combines multiple avatars into a stack:

Note that you must not wrap child Avatar components with any additional elements, but you can use wrap Avatar with components that do not render any HTML elements in the current tree, for example Tooltip.

Example of usage with Tooltip:

Avatar is a polymorphic component – its default root element is div, but it can be changed to any other element or component with component prop:

You can also use components in component prop, for example, Next.js Link:

Polymorphic components with TypeScript

Note that polymorphic components props types are different from regular components – they do not extend HTML element props of the default element. For example, AvatarProps does not extend React.ComponentPropsWithoutRef'<'div'>' although div is the default element.

If you want to create a wrapper for a polymorphic component that is not polymorphic (does not support component prop), then your component props interface should extend HTML element props, for example:

If you want your component to remain polymorphic after wrapping, use createPolymorphicComponent function described in this guide.

Example using Avatar as a link:

Avatar renders <img /> HTML element. Set alt prop to describe image, it i

*[Content truncated - see full docs]*

**Examples**:

```python
import { Avatar } from '@mantine/core';
import { IconStar } from '@tabler/icons-react';

function Demo() {
  return (
    <>
      {/* With image */}
      <Avatar src="avatar.png" alt="it's me" />

      {/* Default placeholder */}
      <Avatar radius="xl" />

      {/* Letters with xl radius */}
      <Avatar color="cyan" radius="xl">MK</Avatar>

      {/* Custom placeholder icon */}
      <Avatar color="blue" radius="sm">
        <IconStar size={20} />
      </Avatar>
    </>
  );
}
```

```python
import { Avatar, Group } from '@mantine/core';

const names = [
  'John Doe',
  'Jane Mol',
  'Alex Lump',
  'Sarah Condor',
  'Mike Johnson',
  'Kate Kok',
  'Tom Smith',
];

function Demo() {
  const avatars = names.map((name) => <Avatar key={name} name={name} color="initials" />);
  return <Group>{avatars}</Group>;
}
```

```python
import { Avatar, Group } from '@mantine/core';

const names = [
  'John Doe',
  'Jane Mol',
  'Alex Lump',
  'Sarah Condor',
  'Mike Johnson',
  'Kate Kok',
  'Tom Smith',
];

function Demo() {
  const avatars = names.map((name) => (
    <Avatar key={name} name={name} color="initials" allowedInitialsColors={['blue', 'red']} />
  ));
  return <Group>{avatars}</Group>;
}
```

---

## BackgroundImage | Mantine

**URL**: https://mantine.dev/core/background-image/

**Contents**:
- BackgroundImage
- Usage
- Polymorphic component

Displays image as background

BackgroundImage component can be used to add any content on image. It is useful for hero headers and other similar sections

BackgroundImage is a polymorphic component – its default root element is div, but it can be changed to any other element or component with component prop:

Polymorphic components with TypeScript

Note that polymorphic components props types are different from regular components – they do not extend HTML element props of the default element. For example, BackgroundImageProps does not extend React.ComponentPropsWithoutRef'<'div'>' although div is the default element.

If you want to create a wrapper for a polymorphic component that is not polymorphic (does not support component prop), then your component props interface should extend HTML element props, for example:

If you want your component to remain polymorphic after wrapping, use createPolymorphicComponent function described in this guide.

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { BackgroundImage, Center, Text, Box } from '@mantine/core';

function Demo() {
  return (
    <Box maw={300} mx="auto">
      <BackgroundImage
        src="https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/images/bg-6.png"
        radius="sm"
      >
        <Center p="md">
          <Text c="white">
            BackgroundImage component can be used to add any content on image. It is useful for hero
            headers and other similar sections
          </Text>
        
...
```

```python
import { BackgroundImage } from '@mantine/core';

function Demo() {
  return <BackgroundImage component="button" />;
}
```

```python
import type { BackgroundImageProps, ElementProps } from '@mantine/core';

interface MyBackgroundImageProps extends BackgroundImageProps,
  ElementProps<'button', keyof BackgroundImageProps> {}
```

---

## Badge | Mantine

**URL**: https://mantine.dev/core/badge/

**Contents**:
- Badge
- Usage
- Gradient variant
- Rounded
- Left and right sections
- Full width
- Customize variants colors
- autoContrast

Display badge, pill or tag

When variant prop is set to gradient, you can control gradient with gradient prop, it accepts an object with from, to and deg properties. If thegradient prop is not set, Badge will use theme.defaultGradient which can be configured on the theme object. gradient prop is ignored when variant is not gradient.

Note that variant="gradient" supports only linear gradients with two colors. If you need a more complex gradient, then use Styles API to modify Badge styles.

Set circle prop, to reduce horizontal padding and make badge width equal to its height:

Set fullWidth to make badge span full width of its parent element:

You can customize colors for Badge and other components variants by adding variantColorResolver to your theme.

Badge supports autoContrast prop and theme.autoContrast. If autoContrast is set either on Badge or on theme, content color will be adjusted to have sufficient contrast with the value specified in color prop.

Note that autoContrast feature works only if you use color prop to change background color. autoContrast works only with filled variant.

Badge supports Styles API, you can add styles to any inner element of the component withclassNames prop. Follow Styles API documentation to learn more.

Hover over selectors to highlight corresponding elements

Left and right sections

Badge is a polymorphic component – its default root element is div, but it can be changed to any other element or component with component prop:

You can also use components in component prop, for example, Next.js Link:

Polymorphic components with TypeScript

Note that polymorphic components props types are different from regular components – they do not extend HTML element props of the default element. For example, BadgeProps does not extend React.ComponentPropsWithoutRef'<'div'>' although div is the default element.

If you want to create a wrapper for a polymorphic component that is not polymorphic (does not support component prop), then you

*[Content truncated - see full docs]*

**Examples**:

```python
import { Badge } from '@mantine/core';

function Demo() {
  return <Badge color="blue">Badge</Badge>;
}
```

```python
import { Badge } from '@mantine/core';

function Demo() {
  return (
    <Badge
      size="xl"
      variant="gradient"
      gradient={{ from: 'blue', to: 'cyan', deg: 90 }}
    >
      Gradient badge
    </Badge>
  );
}
```

```python
import { Badge, Group } from '@mantine/core';

function Demo() {
  return (
    <Group>
      <Badge size="xs" circle>
        1
      </Badge>
      <Badge size="sm" circle>
        7
      </Badge>
      <Badge size="md" circle>
        9
      </Badge>
      <Badge size="lg" circle>
        3
      </Badge>
      <Badge size="xl" circle>
        8
      </Badge>
    </Group>
  );
}
```

---

## Blockquote | Mantine

**URL**: https://mantine.dev/core/blockquote/

**Contents**:
- Blockquote
- Usage

Blockquote with optional cite

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { Blockquote } from '@mantine/core';
import { IconInfoCircle } from '@tabler/icons-react';

function Demo() {
  const icon = <IconInfoCircle />;
  return (
    <Blockquote color="blue" cite="– Forrest Gump" icon={icon} mt="xl">
      Life is like an npm install – you never know what you are going to get.
    </Blockquote>
  );
}
```

---

## Box | Mantine

**URL**: https://mantine.dev/core/box/

**Contents**:
- Box
- Usage

Base component for all Mantine components

Box component is used as a base for all other components. Box supports the following features:

You can use Box as a base for your own components or as a replacement for HTML elements:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { Box } from '@mantine/core';

function Demo() {
  return (
    <Box bg="red.5" my="xl" component="a" href="/">
      My component
    </Box>
  );
}
```

---

## Burger | Mantine

**URL**: https://mantine.dev/core/burger/

**Contents**:
- Burger
- Usage
- Change lines size
- Get element ref
- Accessibility

Open/close navigation button

Burger component renders open/close menu button. Set opened and onClick props to control component state. If opened prop is set, cross will be rendered, otherwise – burger.

To make Burger accessible for screen readers, you need to either set aria-label or use VisuallyHidden component:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { useDisclosure } from '@mantine/hooks';
import { Burger } from '@mantine/core';

function Demo() {
  const [opened, { toggle }] = useDisclosure();
  return <Burger opened={opened} onClick={toggle} aria-label="Toggle navigation" />;
}
```

```python
import { useDisclosure } from '@mantine/hooks';
import { Burger } from '@mantine/core';

function Demo() {
  const [opened, { toggle }] = useDisclosure();
  return <Burger lineSize={2} size="xl" opened={opened} onClick={toggle} aria-label="Toggle navigation" />;
}
```

```python
import { useRef } from 'react';
import { Burger } from '@mantine/core';

function Demo() {
  const ref = useRef<HTMLButtonElement>(null);
  return <Burger ref={ref} />;
}
```

---

## Button | Mantine

**URL**: https://mantine.dev/core/button/

**Contents**:
- Button
- Usage
- Full width
- Left and right sections
- Sections position
- Compact size
- Gradient variant
- Disabled state

Button component to render button or link

If fullWidth prop is set Button will take 100% of parent width:

leftSection and rightSection allow adding icons or any other element to the left and right side of the button. When a section is added, padding on the corresponding side is reduced.

Note that leftSection and rightSection are flipped in RTL mode (leftSection is displayed on the right and rightSection is displayed on the left).

justify prop sets justify-content of inner element. You can use it to change the alignment of left and right sections. For example, to spread them across the button set justify="space-between".

If you need to align just one section to the side of the button set justify to space-between and add empty <span /> to the opposite section.

Button supports xs – xl and compact-xs – compact-xl sizes. compact sizes have the same font-size as xs – xl but reduced padding and height.

When variant prop is set to gradient, you can control gradient with gradient prop, it accepts an object with from, to and deg properties. If thegradient prop is not set, Button will use theme.defaultGradient which can be configured on the theme object. gradient prop is ignored when variant is not gradient.

Note that variant="gradient" supports only linear gradients with two colors. If you need a more complex gradient, then use Styles API to modify Button styles.

To make Button disabled, set disabled prop, this will prevent any interactions with the button and add disabled styles. If you want the button to just look disabled but still be interactive, set data-disabled prop instead. Note that disabled styles are the same for all variants.

<a /> element does not support disabled attribute. To make Button disabled when it is rendered as a link, set data-disabled attribute instead and prevent default behavior in onClick event handler.

To customize disabled styles, it is recommended to use both &:disabled and &[data-disabled] selectors:

onMouseLeave event is not trigge

*[Content truncated - see full docs]*

**Examples**:

```python
import { Button } from '@mantine/core';

function Demo() {
  return <Button variant="filled">Button</Button>;
}
```

```python
import { Button } from '@mantine/core';

function Demo() {
  return <Button fullWidth>Full width button</Button>;
}
```

```python
import { Group, Button } from '@mantine/core';
import { IconPhoto, IconDownload, IconArrowRight } from '@tabler/icons-react';

function Demo() {
  return (
    <Group justify="center">
      <Button leftSection={<IconPhoto size={14} />} variant="default">
        Gallery
      </Button>

      <Button rightSection={<IconDownload size={14} />}>Download</Button>

      <Button
        variant="light"
        leftSection={<IconPhoto size={14} />}
        rightSection={<IconArrowRight size={14} />}

...
```

---

## CSS files list | Mantine

**URL**: https://mantine.dev/styles/css-files-list/

**Contents**:
- CSS files list
- Components dependencies
- Global styles
- Import order
- Files list

This page contains a list of CSS files that you can import from @mantine/core package as a replacement for @mantine/core/styles.css.

Some components require additional styles to work properly. For example, Button component is based on UnstyledButton. If you want to use Button, you need to import styles for UnstyledButton as well.

Some components like Select do not have any styles on their own – they are built on top of other components. To find out which components are used in a particular component, check the component source code.

If you are not sure which components are used in a particular component, you can import all styles for components that are reused in other components:

All Mantine components depend on global styles, you need to import them before all other styles:

It is important to keep correct styles import order. For example, if you want to use Button component, you need to import styles for UnstyledButton first and then import styles for Button.

Note that if you cannot find a particular file in the list below, it means that the component does not have any styles on its own or it is built on top of other components.

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```text
import '@mantine/core/styles/UnstyledButton.css';
import '@mantine/core/styles/Button.css';
```

```text
import '@mantine/core/styles/ScrollArea.css';
import '@mantine/core/styles/UnstyledButton.css';
import '@mantine/core/styles/VisuallyHidden.css';
import '@mantine/core/styles/Paper.css';
import '@mantine/core/styles/Popover.css';
import '@mantine/core/styles/CloseButton.css';
import '@mantine/core/styles/Group.css';
import '@mantine/core/styles/Loader.css';
import '@mantine/core/styles/Overlay.css';
import '@mantine/core/styles/ModalBase.css';
import '@mantine/core/styles/Input.css';
import '@ma
...
```

```text
import '@mantine/core/styles/baseline.css';
import '@mantine/core/styles/default-css-variables.css';
import '@mantine/core/styles/global.css';
```

---

## Card | Mantine

**URL**: https://mantine.dev/core/card/

**Contents**:
- Card
- Usage
- Polymorphic component
- Card.Section
- Polymorphic Card.Section
- withBorder and inheritPadding props

Card is a wrapper around Paper component with some additional styles and Card.Section component that allows to split card into sections. If you do not need sections, you use Paper component instead.

Norway Fjord Adventures

With Fjord Tours you can explore more of the magical fjord landscapes with tours and activities on and around the fjords of Norway

Card is a polymorphic component component, you can change its root element:

You've won a million dollars in cash!

Please click anywhere on this card to claim your reward, this is not a fraud, trust us

Card.Section is a special component that is used to remove Card padding from its children while other elements still have horizontal spacing. Card.Section works the following way:

Note that Card relies on mapping direct children and you cannot use fragments or other wrappers for Card.Section:

Card.Section is a polymorphic component component, you can change its root element:

Norway Fjord Adventures

With Fjord Tours you can explore more of the magical fjord landscapes with tours and activities on and around the fjords of Norway

200+ images uploaded since last visit, review them to select which one should be added to your gallery

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { Card, Image, Text, Badge, Button, Group } from '@mantine/core';

function Demo() {
  return (
    <Card shadow="sm" padding="lg" radius="md" withBorder>
      <Card.Section>
        <Image
          src="https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/images/bg-8.png"
          height={160}
          alt="Norway"
        />
      </Card.Section>

      <Group justify="space-between" mt="md" mb="xs">
        <Text fw={500}>Norway Fjord Adventures</Text>
        <Badge c
...
```

```python
import { Card, Image, Text } from '@mantine/core';

function Demo() {
  return (
    <Card
      shadow="sm"
      padding="xl"
      component="a"
      href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
      target="_blank"
    >
      <Card.Section>
        <Image
          src="https://images.unsplash.com/photo-1579227114347-15d08fc37cae?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=2550&q=80"
          h={160}
          alt="No way!"
        />
   
...
```

```python
import { Card, Text } from '@mantine/core';

function Demo() {
  return (
    <Card padding="xl">
      {/* top, right, left margins are negative – -1 * theme.spacing.xl */}
      <Card.Section>First section</Card.Section>

      {/* Content that is not inside Card.Section will have theme.spacing.xl spacing on all sides relative to Card */}
      <Text>Some other content</Text>

      {/* right, left margins are negative – -1 * theme.spacing.xl */}
      <Card.Section>Middle section</Card.Sectio
...
```

---

## Center | Mantine

**URL**: https://mantine.dev/core/center/

**Contents**:
- Center
- Usage
- Inline
- Polymorphic component

Centers content vertically and horizontally

To use Center with inline elements set inline prop. For example, you can center link icon and label:

Center is a polymorphic component – its default root element is div, but it can be changed to any other element or component with component prop:

Polymorphic components with TypeScript

Note that polymorphic components props types are different from regular components – they do not extend HTML element props of the default element. For example, CenterProps does not extend React.ComponentPropsWithoutRef'<'div'>' although div is the default element.

If you want to create a wrapper for a polymorphic component that is not polymorphic (does not support component prop), then your component props interface should extend HTML element props, for example:

If you want your component to remain polymorphic after wrapping, use createPolymorphicComponent function described in this guide.

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { Center, Box } from '@mantine/core';

function Demo() {
  return (
    <Center maw={400} h={100} bg="var(--mantine-color-gray-light)">
      <Box bg="var(--mantine-color-blue-light)">All elements inside Center are centered</Box>
    </Center>
  );
}
```

```python
import { Center, Anchor, Box } from '@mantine/core';
import { IconArrowLeft } from '@tabler/icons-react';

function Demo() {
  return (
    <Anchor href="https://mantine.dev" target="_blank">
      <Center inline>
        <IconArrowLeft size={12} />
        <Box ml={5}>Back to Mantine website</Box>
      </Center>
    </Anchor>
  );
}
```

```python
import { Center } from '@mantine/core';

function Demo() {
  return <Center component="button" />;
}
```

---

## Checkbox | Mantine

**URL**: https://mantine.dev/core/checkbox/

**Contents**:
- Checkbox
- Usage
- Controlled
- States
- Change icons
- Change icon color
- Indeterminate state
- Label with link

Capture boolean input from user

Use iconColor prop to change icon color. You can reference colors from theme.colors or use any valid CSS color:

Checkbox supports indeterminate state. When indeterminate prop is set, checked prop is ignored (checkbox always has checked styles):

You can change target element to which tooltip is attached with refProp:

By default, checkbox input and label have cursor: default (same as native input[type="checkbox"]). To change cursor to pointer, set cursorType on theme:

You can add any number of custom sizes with data-size attribute:

All props passed to the component are forwarded to the input element. If you need to add props to the root element, use wrapperProps. In the following example:

Checkbox.Indicator looks exactly the same as Checkbox component, but it does not have any semantic meaning, it's just a visual representation of checkbox state. You can use it in any place where you need to display checkbox state without any interaction related to the indicator. For example, it is useful in cards based on buttons, trees, etc.

Note that Checkbox.Indicator cannot be focused or selected with keyboard. It is not accessible and should not be used as a replacement for Checkbox component.

Checkbox.Card component can be used as a replacement for Checkbox to build custom cards/buttons/other things that work as checkboxes. The root element of the component has role="checkbox" attribute, it is accessible by default and supports the same keyboard interactions as input[type="checkbox"].

Core components library: inputs, buttons, overlays, etc.

You can use Checkbox.Card with Checkbox.Group the same way as Checkbox component:

Choose all packages that you will need in your application

Core components library: inputs, buttons, overlays, etc.

Collection of reusable hooks for React applications.

@mantine/notifications

Checkbox supports Styles API, you can add styles to any inner element of the component withclassNames prop. Follow Styles A

*[Content truncated - see full docs]*

**Examples**:

```python
import { Checkbox } from '@mantine/core';

function Demo() {
  return (
    <Checkbox
      defaultChecked
      label="I agree to sell my privacy"
    />
  );
}
```

```python
import { useState } from 'react';
import { Checkbox } from '@mantine/core';

function Demo() {
  const [checked, setChecked] = useState(false);
  return (
    <Checkbox
      checked={checked}
      onChange={(event) => setChecked(event.currentTarget.checked)}
    />
  );
}
```

```python
import { Checkbox, Stack } from '@mantine/core';

function Demo() {
  return (
    <Stack>
      <Checkbox checked={false} onChange={() => {}} label="Default checkbox" />
      <Checkbox checked={false} onChange={() => {}} indeterminate label="Indeterminate checkbox" />
      <Checkbox checked onChange={() => {}} label="Checked checkbox" />
      <Checkbox checked variant="outline" onChange={() => {}} label="Outline checked checkbox" />
      <Checkbox
        variant="outline"
        onChange=
...
```

---

## Chip | Mantine

**URL**: https://mantine.dev/core/chip/

**Contents**:
- Chip
- Usage
- Controlled
- Change checked icon
- States
- Chip with tooltip
- Add props to the root element
- Chip.Group

Pick one or multiple values with inline controls

To use Chip with Tooltip and other similar components, set refProp="rootRef" on the Tooltip component:

All props passed to the component are forwarded to the input element. If you need to add props to the root element, use wrapperProps. In the following example:

Chip.Group component manages state of child Chip components, set multiple prop to allow multiple chips to be selected at a time:

Chip and Chip.Group components are accessible by default – they are built with native radio/checkbox inputs, all keyboard events work the same as with native controls.

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { Chip } from '@mantine/core';

function Demo() {
  return <Chip defaultChecked>Awesome chip</Chip>
}
```

```python
import { useState } from 'react';
import { Chip } from '@mantine/core';

function Demo() {
  const [checked, setChecked] = useState(false);

  return (
    <Chip checked={checked} onChange={() => setChecked((v) => !v)}>
      My chip
    </Chip>
  );
}
```

```python
import { Chip } from '@mantine/core';
import { IconX } from '@tabler/icons-react';

function Demo() {
  return (
    <Chip
      icon={<IconX size={16} />}
      color="red"
      variant="filled"
      defaultChecked
    >
      Forbidden
    </Chip>
  );
}
```

---

## CloseButton | Mantine

**URL**: https://mantine.dev/core/close-button/

**Contents**:
- CloseButton
- Usage
- Change icon
- Accessibility

Button with close icon

CloseButton renders a button with X icon inside. It is used in other Mantine components like Drawer or Modal.

You can change icon by passing any react node to the icon prop. It is useful when CloseButton is used as a part of other components, for example, in Drawer or Modal. Note that if you use icon prop, iconSize prop is ignored – you will have to set icon size manually.

To make CloseButton accessible for screen readers, you need to either set aria-label or use VisuallyHidden component:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { CloseButton } from '@mantine/core';

function Demo() {
  return <CloseButton />;
}
```

```python
import { IconXboxX } from '@tabler/icons-react';
import { CloseButton } from '@mantine/core';

function Demo() {
  return <CloseButton icon={<IconXboxX size={18} stroke={1.5} />} />;
}
```

```python
import { CloseButton, VisuallyHidden } from '@mantine/core';

function Demo() {
  return (
    <>
      <CloseButton aria-label="Close modal" />

      <CloseButton>
        <VisuallyHidden>Close modal</VisuallyHidden>
      </CloseButton>
    </>
  );
}
```

---

## Collapse | Mantine

**URL**: https://mantine.dev/core/collapse/

**Contents**:
- Collapse
- Usage
- Change transition
- Nested Collapse components

Animate presence with slide down/up transition

From Bulbapedia: Bulbasaur is a small, quadrupedal Pokémon that has blue-green skin with darker patches. It has red eyes with white pupils, pointed, ear-like structures on top of its head, and a short, blunt snout with a wide mouth. A pair of small, pointed teeth are visible in the upper jaw when its mouth is open. Each of its thick legs ends with three sharp claws. On Bulbasaur's back is a green plant bulb, which is grown from a seed planted there at birth. The bulb also conceals two slender, tentacle-like vines and provides it with energy through photosynthesis as well as from the nutrient-rich seeds contained within.

Set following props to control transition:

From Bulbapedia: Bulbasaur is a small, quadrupedal Pokémon that has blue-green skin with darker patches. It has red eyes with white pupils, pointed, ear-like structures on top of its head, and a short, blunt snout with a wide mouth. A pair of small, pointed teeth are visible in the upper jaw when its mouth is open. Each of its thick legs ends with three sharp claws. On Bulbasaur's back is a green plant bulb, which is grown from a seed planted there at birth. The bulb also conceals two slender, tentacle-like vines and provides it with energy through photosynthesis as well as from the nutrient-rich seeds contained within.

This collapse contains another collapse

Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ea atque in est quaerat dolore odio! Quibusdam, a nihil modi, maiores consequuntur ex quod suscipit illum ducimus doloribus odit commodi tenetur.

This collapse is inside another collapse

Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ea atque in est quaerat dolore odio! Quibusdam, a nihil modi, maiores consequuntur ex quod suscipit illum ducimus doloribus odit commodi tenetur.

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { Button, Group, Text, Collapse, Box } from '@mantine/core';
import { useDisclosure } from '@mantine/hooks';

function Demo() {
  const [opened, { toggle }] = useDisclosure(false);

  return (
    <Box maw={400} mx="auto">
      <Group justify="center" mb={5}>
        <Button onClick={toggle}>Toggle content</Button>
      </Group>

      <Collapse in={opened}>
        <Text>{/* ... content */}</Text>
      </Collapse>
    </Box>
  );
}
```

```python
import { useDisclosure } from '@mantine/hooks';
import { Button, Group, Text, Collapse, Box } from '@mantine/core';

function Demo() {
  const [opened, { toggle }] = useDisclosure(false);

  return (
    <Box maw={400} mx="auto">
      <Group justify="center" mb={5}>
        <Button onClick={toggle}>Toggle with linear transition</Button>
      </Group>

      <Collapse in={opened} transitionDuration={1000} transitionTimingFunction="linear">
        <Text>{/* ...content */}</Text>
      </Collaps
...
```

---

## ColorInput | Mantine

**URL**: https://mantine.dev/core/color-input/

**Contents**:
- ColorInput
- Usage
- Controlled
- Formats
- Preserve invalid input
- onChangeEnd
- Disable free input
- With swatches

Capture color from user

ColorInput component supports Input and Input.Wrapper components features and all input element props. ColorInput documentation does not include all features supported by the component – see Input documentation to learn about all available features.

Component supports hex, hexa, rgb, rgba, hsl and hsla color formats. Slider to change opacity is displayed only for hexa, rgba and hsla formats:

By default, ColorInput will revert the value on blur to the last known valid value. To change this behavior and keep invalid value, set fixOnBlur={false}:

onChangeEnd is called when user stops dragging slider or changes input value. It is useful when you need to update color only when user finished interaction with the component:

Change end value: #FFFFFF

To disable free input set disallowInput prop:

You can add any amount of predefined color swatches:

By default, there will be 7 swatches per row, you can change this with swatchesPerRow prop, like in ColorPicker component:

If you need to restrict color picking to certain colors – disable color picker and disallow free input:

To close the dropdown when one of the color swatches is clicked, set closeOnColorSwatchClick prop:

To hide dropdown, set withPicker={false}:

By default, if EyeDropper API is available, eye dropper icon will be displayed at the right section of the input. To disable it, set withEyeDropper={false}:

You can replace eye dropper icon with any React node using eyeDropperIcon prop:

ColorInput supports leftSection and rightSection props. These sections are rendered with absolute position inside the input wrapper. You can use them to display icons, input controls or any other elements.

You can use the following props to control sections styles and content:

Note that by default, ColorPicker has color preview in the left section and eye dropper button in the right section. You can replace these elements with any React node using leftSection and rightSection props:

ColorInput sup

*[Content truncated - see full docs]*

**Examples**:

```python
import { ColorInput } from '@mantine/core';

function Demo() {
  return (
    <ColorInput
      label="Input label"
      description="Input description"
      placeholder="Input placeholder"
    />
  );
}
```

```python
import { useState } from 'react';
import { ColorInput } from '@mantine/core';

function Demo() {
  const [value, setValue] = useState('');
  return <ColorInput value={value} onChange={setValue} />;
}
```

```python
import { ColorInput } from '@mantine/core';

function Demo() {
  return <ColorInput defaultValue="#C5D899" />;
}
```

---

## Combobox | Mantine

**URL**: https://mantine.dev/core/combobox/

**Contents**:
- Combobox
- Examples
- Usage
- useCombobox hook
- useCombobox options
- Combobox store
- useCombobox handlers
- Combobox.Target

Create custom select, autocomplete or multiselect inputs

This page contains only a small set of examples, as the full code of the demos is long. You can find all 50+ examples on a separate page.

Combobox provides a set of components and hooks to custom select, multiselect or autocomplete components. The component is very flexible – you have full control of the rendering and logic.

useCombobox hook provides combobox store. The store contains the current state of the component and handlers to update it. Created store must be passed to the store prop of Combobox:

useCombobox hooks accepts an options object with the following properties:

You can import UseComboboxOptions type from @mantine/core package:

Combobox store is an object with the following properties:

You can import ComboboxStore type from @mantine/core package:

Combobox store handlers can be used to control Combobox state. For example, to open the dropdown, call openDropdown handler:

You can use store handlers in useCombobox options. For example, you can call selectFirstOption when the dropdown is opened and resetSelectedOption when it is closed:

Combobox.Target should be used as a wrapper for the target element or component. Combobox.Target marks its child as a target for dropdown and sets aria-* attributes and adds keyboard event listeners to it.

Combobox.Target requires a single child element or component. The child component must accept ref and ...others props. You can use any Mantine component as a target without any additional configuration, for example, Button, TextInput or InputBase.

Example of using Combobox.Target with TextInput component:

Example of using Combobox.Target with Button component:

In some cases, you might need to use different elements as an events target and as a dropdown. Use Combobox.EventsTarget to add aria-* attributes and keyboard event handlers, and Combobox.DropdownTarget to position the dropdown relative to the target.

You can have as many Combobox.EventsTarget 

*[Content truncated - see full docs]*

**Examples**:

```python
import { useState } from 'react';
import { Input, InputBase, Combobox, useCombobox } from '@mantine/core';

const groceries = ['🍎 Apples', '🍌 Bananas', '🥦 Broccoli', '🥕 Carrots', '🍫 Chocolate'];

function Demo() {
  const combobox = useCombobox({
    onDropdownClose: () => combobox.resetSelectedOption(),
  });

  const [value, setValue] = useState<string | null>(null);

  const options = groceries.map((item) => (
    <Combobox.Option value={item} key={item}>
      {item}
    </Combobox.Option>
 
...
```

```python
import { Combobox, useCombobox } from '@mantine/core';

function Demo() {
  const combobox = useCombobox();
  return (
    <Combobox store={combobox}>{/* Your implementation */}</Combobox>
  );
}
```

```text
interface UseComboboxOptions {
  /** Default value for `dropdownOpened`, `false` by default */
  defaultOpened?: boolean;

  /** Controlled `dropdownOpened` state */
  opened?: boolean;

  /** Called when `dropdownOpened` state changes */
  onOpenedChange?(opened: boolean): void;

  /** Called when dropdown closes with event source: keyboard, mouse or unknown */
  onDropdownClose?(eventSource: ComboboxDropdownEventSource): void;

  /** Called when dropdown opens with event source: keyboard, mous
...
```

---

## Container | Mantine

**URL**: https://mantine.dev/core/container/

**Contents**:
- Container
- Grid strategy
- Usage
- Fluid
- Customize sizes
- Responsive max-width

Center content with padding and max-width

Starting from 8.2.0, Container supports strategy="grid" prop which enables more features.

Differences from the default strategy="block":

Features supported by strategy="grid":

Example of using breakout feature:

Container centers content and limits its max-width to the value specified in size prop. Note that the size prop does not make max-width responsive, for example, when it set to lg it will always be lg regardless of screen size.

Set fluid prop to make container fluid, it will take 100% of available width, it is the same as setting size="100%".

You can customize existing Container sizes and add new ones with CSS variables on theme:

To make Container max-width responsive, use Styles API to set classNames. For example, you can add responsive size that will make Container max-width different depending on screen size:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { Box, Container } from '@mantine/core';

function Demo() {
  return (
    <Container strategy="grid" size={500}>
      <Box bg="var(--mantine-color-indigo-light)" h={50}>
        Main content
      </Box>

      <Box data-breakout bg="var(--mantine-color-indigo-light)" mt="xs">
        <div>Breakout</div>

        <Box data-container bg="indigo" c="white" h={50}>
          <div>Container inside breakout</div>
        </Box>
      </Box>
    </Container>
  );
}
```

```python
import { Container } from '@mantine/core';

function Demo() {
  const demoProps = {
    bg: 'var(--mantine-color-blue-light)',
    h: 50,
    mt: 'md',
  };

  return (
    <>
      <Container {...demoProps}>Default Container</Container>

      <Container size="xs" {...demoProps}>
        xs Container
      </Container>

      <Container px={0} size={480} {...demoProps}>
        480px Container without padding
      </Container>
    </>
  );
}
```

```python
import { Container } from '@mantine/core';

function Demo() {
  return (
    <Container fluid h={50} bg="var(--mantine-color-blue-light)">
      Fluid container has 100% max-width
    </Container>
  );
}
```

---

## Divider | Mantine

**URL**: https://mantine.dev/core/divider/

**Contents**:
- Divider
- Usage
- Variants
- With label
- Sizes
- Vertical orientation

Horizontal line with optional label or vertical divider

Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aperiam, officiis! Fugit minus ea, perferendis eum consectetur quae vitae. Aliquid, quam reprehenderit? Maiores sed pariatur aliquid commodi atque sunt officiis natus?

Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aperiam, officiis! Fugit minus ea, perferendis eum consectetur quae vitae. Aliquid, quam reprehenderit? Maiores sed pariatur aliquid commodi atque sunt officiis natus?

Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aperiam, officiis! Fugit minus ea, perferendis eum consectetur quae vitae. Aliquid, quam reprehenderit? Maiores sed pariatur aliquid commodi atque sunt officiis natus?

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { Text, Divider } from '@mantine/core';

function Demo() {
  return (
    <>
      <Text>
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aperiam, officiis! Fugit minus ea,
        perferendis eum consectetur quae vitae. Aliquid, quam reprehenderit? Maiores sed pariatur
        aliquid commodi atque sunt officiis natus?
      </Text>

      <Divider my="md" />

      <Text>
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aperiam, officiis! Fugit minus e
...
```

```python
import { Divider } from '@mantine/core';

function Demo() {
  return (
    <>
      <Divider my="sm" />
      <Divider my="sm" variant="dashed" />
      <Divider my="sm" variant="dotted" />
    </>
  );
}
```

```python
import { Divider, Box, Anchor } from '@mantine/core';
import { IconSearch } from '@tabler/icons-react';

function Demo() {
  return (
    <>
      <Divider my="xs" label="Label on the left" labelPosition="left" />
      <Divider my="xs" label="Label in the center" labelPosition="center" />
      <Divider my="xs" label="Label on the right" labelPosition="right" />
      <Divider
        my="xs"
        variant="dashed"
        labelPosition="center"
        label={
          <>
            <IconS
...
```

---

## Drawer | Mantine

**URL**: https://mantine.dev/core/drawer/

**Contents**:
- Drawer
- Usage
- Position
- Offset
- Customize overlay
- Sizes
- Remove header
- Drawer with scroll

Display overlay area at any side of the screen

Drawer can be placed on left (default), top, right and bottom. Control drawer position with position prop, for example <Drawer position="top" />.

Set offset prop to change drawer offset from the edge of the viewport:

Drawer uses Overlay component, you can set any props that Overlay supports with overlayProps:

You can change drawer width/height (depends on position) by setting size prop to predefined size or any valid width, for example, size="55%" or size={200}:

To remove header set withCloseButton={false}

Drawer is built with Transition component. Use transitionProps prop to customize any Transition properties:

onExitTransitionEnd and onEnterTransitionEnd props can be used to run code after exit/enter transition is finished. For example, this is useful when you want to clear data after drawer is closed:

Drawer uses FocusTrap to trap focus. Add data-autofocus attribute to the element that should receive initial focus.

If you do not want to focus any elements when the drawer is opened, use FocusTrap.InitialFocus component to create a visually hidden element that will receive initial focus:

If you do not add data-autofocus attribute and do not use FocusTrap.InitialFocus, drawer will focus the first focusable element inside it which is usually the close button.

The following props can be used to control Drawer behavior. In most cases it is not recommended to turn these features off – it will make the component less accessible.

Drawer uses react-remove-scroll package to lock scroll. You can pass props down to the RemoveScroll component with removeScrollProps:

Use closeButtonProps to customize close button:

You can use the following compound components to have full control over the Drawer rendering:

Use Drawer.Stack component to render multiple drawers at the same time. Drawer.Stack keeps track of opened drawers, manages z-index values, focus trapping and closeOnEscape behavior. Drawer.Stack is designed to be 

*[Content truncated - see full docs]*

**Examples**:

```python
import { useDisclosure } from '@mantine/hooks';
import { Drawer, Button } from '@mantine/core';

function Demo() {
  const [opened, { open, close }] = useDisclosure(false);

  return (
    <>
      <Drawer opened={opened} onClose={close} title="Authentication">
        {/* Drawer content */}
      </Drawer>

      <Button variant="default" onClick={open}>
        Open Drawer
      </Button>
    </>
  );
}
```

```python
import { useDisclosure } from '@mantine/hooks';
import { Drawer, Button } from '@mantine/core';

function Demo() {
  const [opened, { open, close }] = useDisclosure(false);

  return (
    <>
      <Drawer offset={8} radius="md" opened={opened} onClose={close} title="Authentication">
        {/* Drawer content */}
      </Drawer>

      <Button variant="default" onClick={open}>
        Open Drawer
      </Button>
    </>
  );
}
```

```python
import { useDisclosure } from '@mantine/hooks';
import { Drawer, Button } from '@mantine/core';

function Demo() {
  const [opened, { open, close }] = useDisclosure(false);

  return (
    <>
      <Drawer
        opened={opened}
        onClose={close}
        title="Authentication"
        overlayProps={{ backgroundOpacity: 0.5, blur: 4 }}
      >
        {/* Drawer content */}
      </Drawer>

      <Button variant="default" onClick={open}>
        Open Drawer
      </Button>
    </>
  );
}
```

---

## Dropzone | Mantine

**URL**: https://mantine.dev/x/dropzone/

**Contents**:
- Dropzone
- Installation
- Usage
- Dropzone.Accept, Dropzone.Reject and Dropzone.Idle
- Loading state
- Disabled state
- Open file browser manually
- Enable child pointer event

Capture files from user with drag and drop

After installation import package styles at the root of your application:

Dropzone lets you capture one or more files from user. Component is based on react-dropzone and support all of its core features:

Drag images here or click to select files

Attach as many files as you like, each file should not exceed 5mb

Dropzone.Accept, Dropzone.Reject and Dropzone.Idle components are visible only when the user performs certain action:

Set loading prop to indicate loading state with LoadingOverlay component. When loading props is true user cannot drop or select new files (Dropzone becomes disabled):

Drag images here or click to select files

Attach as many files as you like, each file should not exceed 5mb

If you want to implement your own loading state you can disable Dropzone without LoadingOverlay. Same as with loading, when Dropzone is disabled user cannot drop or select new files:

Drag images here or click to select files

Attach as many files as you like, each file should not exceed 5mb

To open files browser from outside of component use openRef prop to get function that will trigger file browser:

Drag images here or click to select files

Attach as many files as you like, each file should not exceed 5mb

By default, Dropzone disables pointer events on its children for dragging events to work. When activateOnClick={false}, clicking on any children inside Dropzone will not do anything. However, you can set style pointerEvents: 'all' to make children clickable. Note that you need to set these styles only on interactive elements, such as buttons or links.

To specify file types provide an object with the keys set to the mime type and the values as an array of file extensions. Find more examples of accepting specific file types in the react-dropzone documentation.

You can also specify file types by providing an array of mime types to accept prop:

To save some research time you can use MIME_TYPES variable exported from 

*[Content truncated - see full docs]*

**Examples**:

```text
yarn add @mantine/dropzone
```

```text
npm install @mantine/dropzone
```

```text
import '@mantine/core/styles.css';
// ‼️ import dropzone styles after core package styles
import '@mantine/dropzone/styles.css';
```

---

## Flex | Mantine

**URL**: https://mantine.dev/core/flex/

**Contents**:
- Flex
- Usage
- Supported props
- Responsive props
- Difference from Group and Stack
- Browser support

Compose elements in a flex container

Flex component props can have responsive values the same way as other style props:

Flex component is an alternative to Group and Stack. Flex is more flexible, it allows creating both horizontal and vertical flexbox layouts, but requires more configuration. Unlike Group and Stack Flex is polymorphic and supports responsive props.

Flex uses flexbox gap to add spacing between children. In older browsers, Flex children may not have spacing. You can install PostCSS flex-gap-polyfill to add support for older browsers.

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { Flex, Button } from '@mantine/core';

function Demo() {
  return (
    <Flex
      mih={50}
      bg="rgba(0, 0, 0, .3)"
      gap="md"
      justify="flex-start"
      align="flex-start"
      direction="row"
      wrap="wrap"
    >
      <Button>Button 1</Button>
      <Button>Button 2</Button>
      <Button>Button 3</Button>
    </Flex>
  );
}
```

```python
import { Flex, Button } from '@mantine/core';

function Demo() {
  return (
    <Flex
      direction={{ base: 'column', sm: 'row' }}
      gap={{ base: 'sm', sm: 'lg' }}
      justify={{ sm: 'center' }}
    >
      <Button>Button 1</Button>
      <Button>Button 2</Button>
      <Button>Button 3</Button>
    </Flex>
  );
}
```

---

## FloatingIndicator | Mantine

**URL**: https://mantine.dev/core/floating-indicator/

**Contents**:
- FloatingIndicator
- Usage
- Multiple rows
- Example: Tabs

Display a floating indicator over a group of elements

FloatingIndicator is designed to highlight active element in a group. It can be used to create custom segmented controls, tabs and other similar components.

FloatingIndicator renders an element over the target element. To calculate the position it is required to pass parent element which has a relative position.

By default, FloatingIndicator does not have any visible styles. You can use className prop or Styles API to apply styles.

FloatingIndicator can be used to highlight active element in a group with multiple rows:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { useState } from 'react';
import { FloatingIndicator, UnstyledButton } from '@mantine/core';
import classes from './Demo.module.css';

const data = ['React', 'Vue', 'Angular', 'Svelte'];

function Demo() {
  const [rootRef, setRootRef] = useState<HTMLDivElement | null>(null);
  const [controlsRefs, setControlsRefs] = useState<Record<string, HTMLButtonElement | null>>({});
  const [active, setActive] = useState(0);

  const setControlRef = (index: number) => (node: HTMLButtonElement) => {
...
```

```python
import { useState } from 'react';
import {
  IconArrowDown,
  IconArrowDownLeft,
  IconArrowDownRight,
  IconArrowLeft,
  IconArrowRight,
  IconArrowUp,
  IconArrowUpLeft,
  IconArrowUpRight,
  IconCircle,
} from '@tabler/icons-react';
import { FloatingIndicator, UnstyledButton } from '@mantine/core';
import classes from './Demo.module.css';

function Demo() {
  const [rootRef, setRootRef] = useState<HTMLDivElement | null>(null);
  const [controlsRefs, setControlsRefs] = useState<Record<string, 
...
```

```python
import { useState } from 'react';
import { FloatingIndicator, Tabs } from '@mantine/core';
import classes from './Demo.module.css';

function Demo() {
  const [rootRef, setRootRef] = useState<HTMLDivElement | null>(null);
  const [value, setValue] = useState<string | null>('1');
  const [controlsRefs, setControlsRefs] = useState<Record<string, HTMLButtonElement | null>>({});
  const setControlRef = (val: string) => (node: HTMLButtonElement) => {
    controlsRefs[val] = node;
    setControlsRefs(
...
```

---

## FocusTrap | Mantine

**URL**: https://mantine.dev/core/focus-trap/

**Contents**:
- FocusTrap
- Usage
- Initial focus
- FocusTrap.InitialFocus
- Focus trapping logic

Trap focus at child node

FocusTrap is a component implementation of use-focus-trap hook, it is used in all Mantine components that require focus trap (Modal, DatePicker, Popover, etc.).

To define the element that will receive initial focus set data-autofocus attribute:

FocusTrap.InitialFocus is a special component that adds a visually hidden element which will receive the focus when the focus trap is activated. Once FocusTrap.InitialFocus loses focus, it is removed from the tab order.

For example, it is useful if you do not want to focus any elements inside the Modal when it is opened:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { useDisclosure } from '@mantine/hooks';
import { FocusTrap, TextInput, Button, Box } from '@mantine/core';

function Demo() {
  const [active, { toggle }] = useDisclosure(false);

  return (
    <Box maw={400} mx="auto">
      <Button onClick={toggle}>{active ? 'Deactivate' : 'Activate'} focus trap</Button>

      <FocusTrap active={active}>
        <div>
          <TextInput mt="sm" label="First input" placeholder="First input" />
          <TextInput mt="sm" label="Second input" placeh
...
```

```python
import { useDisclosure } from '@mantine/hooks';
import { FocusTrap, TextInput, Button, Box } from '@mantine/core';

function Demo() {
  const [active, { toggle }] = useDisclosure(false);

  return (
    <Box maw={400} mx="auto">
      <Button onClick={toggle}>{active ? 'Deactivate' : 'Activate'} focus trap</Button>

      <FocusTrap active={active}>
        <div>
          <TextInput mt="sm" label="First input" placeholder="First input" />
          <TextInput mt="sm" label="Second input" placeh
...
```

```python
import { useDisclosure } from '@mantine/hooks';
import { Modal, Button, TextInput, FocusTrap } from '@mantine/core';

function Demo() {
  const [opened, { open, close }] = useDisclosure(false);

  return (
    <>
      <Modal opened={opened} onClose={close} title="Focus demo">
        <FocusTrap.InitialFocus />
        <TextInput label="First input" placeholder="First input" />
        <TextInput
          data-autofocus
          label="Input with initial focus"
          placeholder="It has da
...
```

---

## Global styles | Mantine

**URL**: https://mantine.dev/styles/global-styles/

**Contents**:
- Global styles
- CSS reset
- Body and :root elements styles
- Static classes
- Add global styles in your application

@mantine/core package includes some global styles that are required for components to work correctly. If you override these styles, some components might not work as expected.

Global styles are automatically imported with:

If you want to import styles per component, you need to import all global styles manually:

@mantine/core package includes minimal CSS reset – it includes only basic styles required for components to work in modern browsers. If you need to support older browsers, you can additionally include normalize.css or any other CSS reset of your choice.

@mantine/core package includes the following body and :root elements styles:

@mantine/core package includes the following static classes:

You can use these classes with any components or elements:

It is recommended to use CSS modules to apply styles to Mantine components with className prop or with Styles API. CSS modules files names usually end with .module.css, if you want to add global styles to your application, create a file with .css extension but without .module part, for example global.css.

In global .css files you can reference all Mantine CSS variables and change styles of <body />, :root and other elements. For example, to change body background-color:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```text
import '@mantine/core/styles.css';
```

```text
import '@mantine/core/styles/baseline.css';
import '@mantine/core/styles/default-css-variables.css';
import '@mantine/core/styles/global.css';
```

```text
body {
  margin: 0;
}

*,
*::before,
*::after {
  box-sizing: border-box;
}

input,
button,
textarea,
select {
  font: inherit;
}

button,
select {
  text-transform: none;
}
```

---

## Grid | Mantine

**URL**: https://mantine.dev/core/grid/

**Contents**:
- Grid
- Usage
- Columns span
- Gutter
- Grow
- Column offset
- Order
- Multiple rows

Responsive 12 columns grid system

Grid.Col span prop controls the ratio of column width to the total width of the row. By default, grid uses 12 columns layout, so span prop can be any number from 1 to 12.

span prop also supports object syntax to change column width based on viewport width, it accepts xs, sm, md, lg and xl keys and values from 1 to 12. The syntax is the same as in style props.

In the following example span={{ base: 12, md: 6, lg: 3 }}:

Set gutter prop to control spacing between columns. The prop works the same way as style props – you can reference theme.spacing values with xs, sm, md, lg and xl strings and use object syntax to change gutter based on viewport width:

If grow prop is set, column will grow to fill the remaining space in the row:

Set offset prop on Grid.Col component to add gaps to the grid. offset prop supports the same syntax as span prop: a number from 1 to 12 or an object with xs, sm, md, lg and xl keys and values from 1 to 12.

Set the order prop on Grid.Col component to change the order of columns. order prop supports the same syntax as span prop: a number from 1 to 12 or an object with xs, sm, md, lg and xl keys and values from 1 to 12.

Once columns span and offset sum exceeds columns prop (12 by default), columns are moved to the next row:

You can control justify-content and align-items CSS properties with justify and align props on Grid component:

All columns in a row with span="auto" grow as much as they can to fill the row. In the following example, the second column takes up 50% of the row while the other two columns automatically resize to fill the remaining space:

If you set span="content", the column's size will automatically adjust to match the width of its content:

By default, grid uses 12 columns layout, you can change it by setting columns prop on Grid component. Note that in this case, columns span and offset will be calculated relative to this value.

In the following example, first column takes 50% with 1

*[Content truncated - see full docs]*

**Examples**:

```python
import { Grid } from '@mantine/core';

function Demo() {
  return (
    <Grid>
      <Grid.Col span={4}>1</Grid.Col>
      <Grid.Col span={4}>2</Grid.Col>
      <Grid.Col span={4}>3</Grid.Col>
    </Grid>
  );
}
```

```python
import { Grid } from '@mantine/core';

function Demo() {
  return (
    <Grid>
      <Grid.Col span={{ base: 12, md: 6, lg: 3 }}>1</Grid.Col>
      <Grid.Col span={{ base: 12, md: 6, lg: 3 }}>2</Grid.Col>
      <Grid.Col span={{ base: 12, md: 6, lg: 3 }}>3</Grid.Col>
      <Grid.Col span={{ base: 12, md: 6, lg: 3 }}>4</Grid.Col>
    </Grid>
  );
}
```

```python
import { Grid } from '@mantine/core';

function Demo() {
  return (
    <Grid gutter={{ base: 5, xs: 'md', md: 'xl', xl: 50 }}>
      <Grid.Col span={4}>1</Grid.Col>
      <Grid.Col span={4}>2</Grid.Col>
      <Grid.Col span={4}>3</Grid.Col>
    </Grid>
  );
}
```

---

## Image | Mantine

**URL**: https://mantine.dev/core/image/

**Contents**:
- Image
- Usage
- Image height
- Image fit
- Fallback image
- Usage with Next.js Image

Image with optional fallback

Image is a wrapper for img with minimal styles. By default, the image will take 100% of parent width. The image size can be controlled with w and h style props.

In most case, you will need to set image height to prevent layout jumps when image is loading. You can do so with h style props.

By default the image has object-fit: cover style - it will resize to cover parent element. To change this behavior, set w="auto" and fit="contain" props.

Set fallbackSrc prop to display fallback image when image fails to load:

Image component is a polymorphic component, its root element can be changed with component prop. You can use it with next/image and other similar components.

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { Image } from '@mantine/core';

function Demo() {
  return (
    <Image
      radius="md"
      src="https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/images/bg-7.png"
    />
  );
}
```

```python
import { Image } from '@mantine/core';

function Demo() {
  return (
    <Image
      radius="md"
      h={200}
      src="https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/images/bg-10.png"
    />
  );
}
```

```python
import { Image } from '@mantine/core';

function Demo() {
  return (
    <Image
      radius="md"
      h={200}
      w="auto"
      fit="contain"
      src="https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/images/bg-9.png"
    />
  );
}
```

---

## Indicator | Mantine

**URL**: https://mantine.dev/core/indicator/

**Contents**:
- Indicator
- Usage
- Inline
- Offset
- Processing animation
- Disabled

Display element at the corner of another element

When the target element has a fixed width, set inline prop to add display: inline-block; styles to Indicator container. Alternatively, you can set width and height with style prop if you still want the root element to keep display: block.

Set offset to change indicator position. It is useful when Indicator component is used with children that have border-radius:

Set disabled to hide the indicator:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { Indicator, Avatar } from '@mantine/core';

function Demo() {
  return (
    <Indicator>
      <Avatar
        size="lg"
        radius="sm"
        src="https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/avatars/avatar-1.png"
      />
    </Indicator>
  );
}
```

```python
import { Avatar, Indicator } from '@mantine/core';

function Demo() {
  return (
    <Indicator inline label="New" size={16}>
      <Avatar
        size="lg"
        radius="sm"
        src="https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/avatars/avatar-2.png"
      />
    </Indicator>
  );
}
```

```python
import { Avatar, Indicator } from '@mantine/core';

function Demo() {
  return (
    <Indicator inline size={16} offset={7} position="bottom-end" color="red" withBorder>
      <Avatar
        size="lg"
        radius="xl"
        src="https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/avatars/avatar-3.png"
      />
    </Indicator>
  );
}
```

---

## Input | Mantine

**URL**: https://mantine.dev/core/input/

**Contents**:
- Input
- Disclaimer
- Usage
- Left and right sections
- Change input element
- Input.Wrapper component
- inputWrapperOrder
- inputContainer

Base component to create custom inputs

!important: In most cases, you should not use Input in your application. Input is a base for other inputs and was not designed to be used directly. Use Input to create custom inputs, for other cases prefer TextInput or other component.

Input component is used as base for some other inputs (NativeSelect, TextInput, Textarea, etc.). The purpose of the Input is to provide shared styles and features to other inputs.

Input supports leftSection and rightSection props. These sections are rendered with absolute position inside the input wrapper. You can use them to display icons, input controls or any other elements.

You can use the following props to control sections styles and content:

Input is a polymorphic component, the default root element is input, but it can be changed to any other element or component.

Example of using Input as button and select:

Example of using react-imask with Input:

Input.Wrapper component is used in all other inputs (TextInput, NativeSelect, Textarea, etc.) under the hood, you do not need to wrap your inputs with it, as it is already included in all of them. Use Input.Wrapper only when you want to create custom inputs.

inputWrapperOrder allows configuring the order of Input.Wrapper parts. It accepts an array of four elements: label, input, error and description. Note that it is not required to include all of them, you can use only those that you need – parts that are not included will not be rendered.

Description below the input

Error and description are

With inputContainer prop, you can enhance inputs that use Input.Wrapper under the hood, for example, you can add Tooltip to the TextInput when the input is focused:

Tooltip will be relative to the input

All components that are based on Input.Wrapper support required and withAsterisk props. When set to true, both of these props will add a red asterisk to the end of the label. The only difference is whether input element will have required att

*[Content truncated - see full docs]*

**Examples**:

```python
import { Input, TextInput } from '@mantine/core';

// Incorrect usage, input is not accessible
function Incorrect() {
  return (
    <Input.Wrapper label="Input label">
      <Input />
    </Input.Wrapper>
  );
}

// Use TextInput instead of Input everywhere you want to use Input,
// it is accessible by default and includes Input.Wrapper
function Correct() {
  return (
    <TextInput label="Input label" description="Input description" />
  );
}
```

```python
import { Input } from '@mantine/core';

function Demo() {
  return <Input placeholder="Input component" />;
}
```

```python
import { useState } from 'react';
import { Input, CloseButton } from '@mantine/core';
import { IconAt } from '@tabler/icons-react';

function Demo() {
  const [value, setValue] = useState('Clear me');
  return (
    <>
      <Input placeholder="Your email" leftSection={<IconAt size={16} />} />
      <Input
        placeholder="Clearable input"
        value={value}
        onChange={(event) => setValue(event.currentTarget.value)}
        rightSectionPointerEvents="all"
        mt="md"
        ri
...
```

---

## JsonInput | Mantine

**URL**: https://mantine.dev/core/json-input/

**Contents**:
- JsonInput
- Usage
- Controlled
- Input props
- Disabled state
- Styles API
- Get element ref
- Accessibility

Capture json data from user

JsonInput is based on Textarea component, it includes json validation logic and option to format input value on blur:

JsonInput component supports Input and Input.Wrapper components features and all textarea element props. JsonInput documentation does not include all features supported by the component – see Input documentation to learn about all available features.

JsonInput supports Styles API, you can add styles to any inner element of the component withclassNames prop. Follow Styles API documentation to learn more.

Hover over selectors to highlight corresponding elements

Root element of the Input

Left and right sections

Required asterisk element, rendered inside label

If JsonInput is used without label prop, it will not be announced properly by screen reader:

Set aria-label to make the input accessible. In this case label will not be visible, but screen reader will announce it:

If label prop is set, input will be accessible it is not required to set aria-label:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { JsonInput } from '@mantine/core';

function Demo() {
  return (
    <JsonInput
      label="Your package.json"
      placeholder="Textarea will autosize to fit the content"
      validationError="Invalid JSON"
      formatOnBlur
      autosize
      minRows={4}
    />
  );
}
```

```python
import { useState } from 'react';
import { JsonInput } from '@mantine/core';

function Demo() {
  const [value, setValue] = useState('');
  return <JsonInput value={value} onChange={setValue} />;
}
```

```python
import { JsonInput } from '@mantine/core';

function Demo() {
  return (
    <JsonInput
      label="Input label"
      description="Input description"
      placeholder="Input placeholder"
    />
  );
}
```

---

## Kbd | Mantine

**URL**: https://mantine.dev/core/kbd/

**Contents**:
- Kbd
- Usage
- Size

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { Kbd } from '@mantine/core';

function Demo() {
  return (
    <div dir="ltr">
      <Kbd>⌘</Kbd> + <Kbd>Shift</Kbd> + <Kbd>M</Kbd>
    </div>
  );
}
```

```python
import { Kbd } from '@mantine/core';

function Demo() {
  return <Kbd>Shift</Kbd>;
}
```

---

## Loader | Mantine

**URL**: https://mantine.dev/core/loader/

**Contents**:
- Loader
- Usage
- Size prop
- Adding custom loaders
  - Custom CSS only loader
  - Custom SVG loader
- children prop

Indicate loading state

Loader component supports 3 types of loaders: oval, bars and dots by default. All loaders are animated with CSS for better performance.

You can pass any valid CSS values and numbers to size prop. Numbers are treated as px, but converted to rem. For example, size={32} will produce --loader-size: 2rem CSS variable.

Loader component is used in other components (Button, ActionIcon, LoadingOverlay, etc.). You can change loader type with default props by setting type. You can also add a custom CSS or SVG loader with loaders default prop.

Note that in order for size and color props to work with custom loaders, you need to use --loader-size and --loader-color CSS variables in your loader styles.

It is recommended to use CSS only loaders, as SVG based animations may have the following issues:

In your SVG loader, you need to use --loader-size and --loader-color variables the same way as in CSS only custom loader in order for size and color props to work. Usually, you would need to set width and height to var(--loader-size) and fill/stroke to var(--loader-color).

Loader supports children prop. If you pass anything to children, it will be rendered instead of the loader. This is useful when you want to control Loader representation in components that use loaderProps, for example Button, LoadingOverlay, Dropzone.

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { Loader } from '@mantine/core';

function Demo() {
  return <Loader color="blue" />;
}
```

```python
import { Loader } from '@mantine/core';

function Demo() {
  return <Loader size={30} />;
}
```

```python
import { MantineProvider, Loader } from '@mantine/core';
import { CssLoader } from './CssLoader';

const theme = createTheme({
  components: {
    Loader: Loader.extend({
      defaultProps: {
        loaders: { ...Loader.defaultLoaders, custom: CssLoader },
        type: 'custom',
      },
    }),
  },
});

function Demo() {
  return (
    <MantineThemeProvider theme={theme}>
      <Loader />
    </MantineThemeProvider>
  );
}
```

---

## LoadingOverlay | Mantine

**URL**: https://mantine.dev/core/loading-overlay/

**Contents**:
- LoadingOverlay
- Usage
- Loader props
- Custom inline loaders

An overlay with centered loader

LoadingOverlay renders an overlay with a loader over the parent element with relative position. It is usually used to indicate loading state of forms. Note that elements under overlay are still focusable with keyboard, remember to add additional logic to handle this case.

LoadingOverlay rendering is controlled by visible prop:

You can pass props down to the Loader component with loaderProps:

To replace default loader with any custom content, set loaderProps={{ children: <div>Your content</div> }}. You can put any React node inside loaderProps.children:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { useDisclosure } from '@mantine/hooks';
import { LoadingOverlay, Button, Group, Box } from '@mantine/core';

function Demo() {
  const [visible, { toggle }] = useDisclosure(false);

  // Note that position: relative is required
  return (
    <>
      <Box pos="relative">
        <LoadingOverlay visible={visible} zIndex={1000} overlayProps={{ radius: "sm", blur: 2 }} />
        {/* ...other content */}
      </Box>

      <Group justify="center">
        <Button onClick={toggle}>Toggle o
...
```

```python
import { useDisclosure } from '@mantine/hooks';
import { LoadingOverlay, Button, Group, Box } from '@mantine/core';

function Demo() {
  const [visible, { toggle }] = useDisclosure(true);

  // Note that position: relative is required
  return (
    <>
      <Box pos="relative">
        <LoadingOverlay
          visible={visible}
          zIndex={1000}
          overlayProps={{ radius: 'sm', blur: 2 }}
          loaderProps={{ color: 'pink', type: 'bars' }}
        />
        {/* ...other conte
...
```

```python
import { useDisclosure } from '@mantine/hooks';
import { LoadingOverlay, Button, Group, Box } from '@mantine/core';

function Demo() {
  const [visible, { toggle }] = useDisclosure(false);

  return (
    <>
      <Box pos="relative">
        <LoadingOverlay visible={visible} loaderProps={{ children: 'Loading...' }} />
        {/* ...other content */}
      </Box>

      <Group justify="center">
        <Button onClick={toggle}>Toggle overlay</Button>
      </Group>
    </>
  );
}
```

---

## Mantine extensions | Mantine

**URL**: https://mantine.dev/x/extensions/

**Contents**:
- Mantine extensions
- Official extensions
- Community extensions
- Create your own extension

Extensions are packages that provide additional functionality like new components, hooks, or other features. They are built on top of @mantine/hooks and @mantine/core packages.

Official extensions are built by the maintainers of Mantine, these extensions have @mantine/ scope in their package names, for example @mantine/dates or @mantine/carousel.

Official extensions list:

Community extensions are built by the community, they are maintained by the community members and are updated independently from the core Mantine packages and extensions.

Community extensions list:

You are welcome to create your own extension and share it with the community in the list above. To submit a new extension to be featured on this page:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

---

## Mantine styles | Mantine

**URL**: https://mantine.dev/styles/mantine-styles/

**Contents**:
- Mantine styles
- Mantine components styles
- Import styles per component
- Styles import order
- CSS layers
- How CSS layers work
- Loading styles from CDN

This guide explains how to import styles of @mantine/* packages in your application and how to override them with CSS layers in case you do not have a way to control the order of stylesheets in your application.

All Mantine components are built with CSS modules, but all styles are bundled before publishing to npm. To include these styles, you need to import @mantine/{package}/styles.css file in your application. Example with @mantine/core package:

By adding this import, you will have all styles of @mantine/core components in your application.

If you want to reduce CSS bundle size, you can import styles per component. Note that some components have dependencies, for example, Button component uses UnstyledButton component internally, so you need to import styles for both components. You can find a full list of exported styles from @mantine/core package and additional instructions on this page.

Note that individual component styles are available only for @mantine/core package. Other packages have minimal styles that can be imported with @mantine/{package}/styles.css import.

It is important to keep the correct styles import order. @mantine/core package styles must always be imported before any other Mantine package styles:

Your application styles must always be imported after all @mantine/* packages styles:

Some bundlers and frameworks do not allow you to control the order of stylesheets in your application. For example, Next.js does not guarantee styles import order. In this case, you can use CSS layers to ensure that your styles will always override Mantine styles.

All @mantine/* packages that export styles have an additional file in which all styles are wrapped in @layer mantine directive.

These files contain the same styles as styles.css files, but wrapped in @layer mantine directive. Make sure that you do not import both styles.css and styles.layer.css files in your application.

Similar to package styles, you can import individual component styles with @l

*[Content truncated - see full docs]*

**Examples**:

```text
import '@mantine/core/styles.css';
```

```text
import '@mantine/core/styles/UnstyledButton.css';
import '@mantine/core/styles/Button.css';
```

```text
// ✅ Correct order
import '@mantine/core/styles.css';
import '@mantine/dates/styles.css';
// ❌ Incorrect order
import '@mantine/dates/styles.css';
import '@mantine/core/styles.css';
```

---

## Mark | Mantine

**URL**: https://mantine.dev/core/mark/

**Contents**:
- Mark
- Usage

Highlight part of the text

Highlight this chunk of the text

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { Text, Mark } from '@mantine/core';

function Demo() {
  return (
    <Text>
      Highlight <Mark>this chunk</Mark> of the text
    </Text>
  );
}
```

---

## Menu | Mantine

**URL**: https://mantine.dev/core/menu/

**Contents**:
- Menu
- Usage
- Submenus
- Controlled
- Show menu on hover
- Disabled items
- Dropdown position
- Transitions

Combine a list of secondary actions into single interactive area

Dropdown opened state can be controlled with opened and onChange props:

Set trigger="hover" to reveal dropdown when hovers over menu target and dropdown. closeDelay and openDelay props can be used to control open and close delay in ms. Note that:

To make Menu that is revealed on hover accessible on all devices, use trigger="click-hover" instead. The dropdown will be revealed on hover on desktop and on click on mobile devices.

Menu dropdown can be animated with any of premade transitions from Transition component:

By default, Menu.Item renders as button element, to change that set component prop:

Note that the component you pass to component prop should allow spreading props to its root element:

Harriette Spoonlicker

hspoonlicker@outlook.com

Menu supports Styles API, you can add styles to any inner element of the component withclassNames prop. Follow Styles API documentation to learn more.

Hover over selectors to highlight corresponding elements

`Menu.Divider` root element

`Menu.Label` root element

`Menu.Item` root element

Left and right sections of `Menu.Item`

Menu.Target requires an element or a component as a single child – strings, fragments, numbers and multiple elements/components are not supported and will throw error. Custom components must provide a prop to get root element ref, all Mantine components support ref out of the box.

Custom components that are rendered inside Menu.Target are required to support ref prop:

Use forwardRef function to forward ref to root element:

Menu follows WAI-ARIA recommendations:

Uncontrolled Menu with trigger="click" (default) will be accessible only when used with button element or component that renders it (Button, ActionIcon, etc.). Other elements will not support Space and Enter key presses.

Menu with trigger="hover" is not accessible – it cannot be accessed with keyboard, use it only if you do not care about accessibility. If you need clic

*[Content truncated - see full docs]*

**Examples**:

```python
import { Menu, Button, Text } from '@mantine/core';
import {
  IconSettings,
  IconSearch,
  IconPhoto,
  IconMessageCircle,
  IconTrash,
  IconArrowsLeftRight,
} from '@tabler/icons-react';

function Demo() {
  return (
    <Menu shadow="md" width={200}>
      <Menu.Target>
        <Button>Toggle menu</Button>
      </Menu.Target>

      <Menu.Dropdown>
        <Menu.Label>Application</Menu.Label>
        <Menu.Item leftSection={<IconSettings size={14} />}>
          Settings
        </Menu.Ite
...
```

```python
import { Button, Menu } from '@mantine/core';

function Demo() {
  return (
    <Menu width={200} position="bottom-start">
      <Menu.Target>
        <Button>Toggle Menu</Button>
      </Menu.Target>

      <Menu.Dropdown>
        <Menu.Item>Dashboard</Menu.Item>

        <Menu.Sub>
          <Menu.Sub.Target>
            <Menu.Sub.Item>Products</Menu.Sub.Item>
          </Menu.Sub.Target>

          <Menu.Sub.Dropdown>
            <Menu.Item>All products</Menu.Item>
            <Menu.Item>Cate
...
```

```python
import { useState } from 'react';
import { Menu } from '@mantine/core';

function Demo() {
  const [opened, setOpened] = useState(false);
  return (
    <Menu opened={opened} onChange={setOpened}>
      {/* Menu content */}
    </Menu>
  );
}
```

---

## Modal | Mantine

**URL**: https://mantine.dev/core/modal/

**Contents**:
- Modal
- Usage
- Center modal vertically
- Remove header
- Change size
- Size auto
- Fullscreen
- Customize overlay

An accessible overlay dialog

To remove header set withCloseButton={false}:

You can change modal width by setting size prop to predefined size or any valid width, for example, 55% or 50rem. Modal width cannot exceed 100vw.

Modal with size="auto" will have width to fit its content:

Fullscreen modal will take the entire screen, it is usually better to change transition to fade when fullScreen prop is set:

To switch Modal to fullscreen on devices with small screens only use use-media-query hook. size prop is ignored if fullScreen prop is set:

Modal uses Overlay component, you can set any props that Overlay supports with overlayProps:

Use xOffset/yOffset to configure horizontal/vertical content offsets:

Modal is built with Transition component. Use transitionProps prop to customize any Transition properties:

onExitTransitionEnd and onEnterTransitionEnd props can be used to run code after exit/enter transition is finished. For example, this is useful when you want to clear data after modal is closed:

Modal uses FocusTrap to trap focus. Add data-autofocus attribute to the element that should receive initial focus.

If you do not want to focus any elements when the modal is opened, use FocusTrap.InitialFocus component to create a visually hidden element that will receive initial focus:

If you do not add data-autofocus attribute and do not use FocusTrap.InitialFocus, modal will focus the first focusable element inside it which is usually the close button.

The following props can be used to control Modal behavior. In most cases, it is not recommended to turn these features off – it will make the component less accessible.

Modal uses react-remove-scroll package to lock scroll. You can pass props down to the RemoveScroll component with removeScrollProps:

Use closeButtonProps to customize close button:

You can use the following compound components to have full control over the Modal rendering:

Use Modal.Stack component to render multiple modals at the same time. 

*[Content truncated - see full docs]*

**Examples**:

```python
import { useDisclosure } from '@mantine/hooks';
import { Modal, Button } from '@mantine/core';

function Demo() {
  const [opened, { open, close }] = useDisclosure(false);

  return (
    <>
      <Modal opened={opened} onClose={close} title="Authentication">
        {/* Modal content */}
      </Modal>

      <Button variant="default" onClick={open}>
        Open modal
      </Button>
    </>
  );
}
```

```python
import { useDisclosure } from '@mantine/hooks';
import { Modal, Button } from '@mantine/core';

function Demo() {
  const [opened, { open, close }] = useDisclosure(false);

  return (
    <>
      <Modal opened={opened} onClose={close} title="Authentication" centered>
        {/* Modal content */}
      </Modal>

      <Button variant="default" onClick={open}>
        Open centered Modal
      </Button>
    </>
  );
}
```

```python
import { useDisclosure } from '@mantine/hooks';
import { Modal, Button } from '@mantine/core';

function Demo() {
  const [opened, { open, close }] = useDisclosure(false);

  return (
    <>
      <Modal opened={opened} onClose={close} withCloseButton={false}>
        Modal without header, press escape or click on overlay to close
      </Modal>

      <Button variant="default" onClick={open}>
        Open modal
      </Button>
    </>
  );
}
```

---

## MultiSelect | Mantine

**URL**: https://mantine.dev/core/multi-select/

**Contents**:
- MultiSelect
- Made with Combobox
- Usage
- Controlled
- Clearable
- Searchable
- Controlled search value
- Nothing found

Custom searchable multi select

MultiSelect is an opinionated component built on top of Combobox component. It has a limited set of features to cover only the basic use cases. If you need more advanced features, you can build your own component with Combobox. You can find examples of custom multi select components on the examples page.

MultiSelect provides a way to enter multiple values. MultiSelect is similar to TagsInput, but it does not allow entering custom values.

MultiSelect value must be an array of strings, other types are not supported. onChange function is called with an array of strings as a single argument.

Set clearable prop to display the clear button in the right section. The button is not displayed when:

Set searchable prop to allow filtering options by user input:

You can control search value with searchValue and onSearchChange props:

Set the nothingFoundMessage prop to display a given message when no options match the search query or there is no data available. If the nothingFoundMessage prop is not set, the MultiSelect dropdown will be hidden.

Set checkIconPosition prop to left or right to control position of check icon in active option. To remove the check icon, set withCheckIcon={false}.

You can limit the number of selected values with maxValues prop. This will not allow adding more values once the limit is reached.

To remove selected options from the list of available options, set hidePickedOptions prop:

MultiSelect data prop accepts data in one of the following formats:

Array of object with value, label and optional disabled keys:

Array of groups with string options:

Array of groups with object options:

Example of a custom filter function that matches options by words instead of letters sequence:

By default, options are sorted by their position in the data array. You can change this behavior with filter function:

The best strategy for large data sets is to limit the number of options that are rendered at the same time. You can 

*[Content truncated - see full docs]*

**Examples**:

```python
import { MultiSelect } from '@mantine/core';

function Demo() {
  return (
    <MultiSelect
      label="Your favorite libraries"
      placeholder="Pick value"
      data={['React', 'Angular', 'Vue', 'Svelte']}
    />
  );
}
```

```python
import { useState } from 'react';
import { MultiSelect } from '@mantine/core';

function Demo() {
  const [value, setValue] = useState<string[]>([]);
  return <MultiSelect data={[]} value={value} onChange={setValue} />;
}
```

```python
import { MultiSelect } from '@mantine/core';

function Demo() {
  return (
    <MultiSelect
      label="Your favorite libraries"
      placeholder="Pick value"
      data={['React', 'Angular', 'Vue', 'Svelte']}
      defaultValue={['React']}
      clearable
    />
  );
}
```

---

## NativeSelect | Mantine

**URL**: https://mantine.dev/core/native-select/

**Contents**:
- NativeSelect
- Usage
- Controlled
- Adding options
  - data prop
  - children options
- With dividers
- Left and right sections

Native select element based on Input

NativeSelect component supports Input and Input.Wrapper components features and all select element props. NativeSelect documentation does not include all features supported by the component – see Input documentation to learn about all available features.

NativeSelect allows passing options in two ways:

Note that if children is used, data will be ignored.

data prop accepts values in one of the following formats:

Example of data prop with array of grouped options:

To add options with children prop, use option elements to add options and optgroup elements to group them:

Use hr tags to add dividers between options:

NativeSelect supports leftSection and rightSection props. These sections are rendered with absolute position inside the input wrapper. You can use them to display icons, input controls or any other elements.

You can use the following props to control sections styles and content:

NativeSelect supports Styles API, you can add styles to any inner element of the component withclassNames prop. Follow Styles API documentation to learn more.

NativeSelect description

Hover over selectors to highlight corresponding elements

Required asterisk element, rendered inside label

Root element of the Input

Left and right sections

If NativeSelect is used without label prop, it will not be announced properly by screen reader:

Set aria-label to make the input accessible. In this case label will not be visible, but screen reader will announce it:

If label prop is set, input will be accessible it is not required to set aria-label:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { NativeSelect } from '@mantine/core';

function Demo() {
  return <NativeSelect label="Input label" description="Input description" data={['React', 'Angular', 'Vue']} />;
}
```

```python
import { useState } from 'react';
import { NativeSelect } from '@mantine/core';

function Demo() {
  const [value, setValue] = useState('');

  return (
    <NativeSelect
      value={value}
      onChange={(event) => setValue(event.currentTarget.value)}
      data={['React', 'Angular', 'Svelte', 'Vue']}
    />
  );
}
```

```python
import { NativeSelect } from '@mantine/core';

function Demo() {
  return (
    <NativeSelect data={['React', 'Angular', 'Svelte', 'Vue']} />
  );
}
```

---

## NavLink | Mantine

**URL**: https://mantine.dev/core/nav-link/

**Contents**:
- NavLink
- Usage
- Active
- autoContrast
- Nested NavLinks
- Polymorphic component
- Get element ref

Set active prop to add active styles to NavLink.

Note that if you're using a React Router NavLink inside renderRoot, the active styles will be based on the aria-current attribute that's set by React Router so you won't need to explicitly set the active prop.

You can customize active styles with color and variant props:

NavLink supports autoContrast prop and theme.autoContrast. If autoContrast is set either on NavLink or on theme, content color will be adjusted to have sufficient contrast with the value specified in color prop.

Note that autoContrast feature works only if you use color prop to change background color. autoContrast works only with filled variant.

To create nested links put NavLink as children of another NavLink:

NavLink is a polymorphic component – its default root element is a, but it can be changed to any other element or component with component prop:

You can also use components in component prop, for example, Next.js Link:

Polymorphic components with TypeScript

Note that polymorphic components props types are different from regular components – they do not extend HTML element props of the default element. For example, NavLinkProps does not extend React.ComponentPropsWithoutRef'<'div'>' although a is the default element.

If you want to create a wrapper for a polymorphic component that is not polymorphic (does not support component prop), then your component props interface should extend HTML element props, for example:

If you want your component to remain polymorphic after wrapping, use createPolymorphicComponent function described in this guide.

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { Badge, NavLink } from '@mantine/core';
import { IconHome2, IconGauge, IconChevronRight, IconActivity, IconCircleOff } from '@tabler/icons-react';

function Demo() {
  return (
    <>
      <NavLink
        href="#required-for-focus"
        label="With icon"
        leftSection={<IconHome2 size={16} stroke={1.5} />}
      />
      <NavLink
        href="#required-for-focus"
        label="With right section"
        leftSection={<IconGauge size={16} stroke={1.5} />}
        rightSection
...
```

```python
import { useState } from 'react';
import { IconGauge, IconFingerprint, IconActivity, IconChevronRight } from '@tabler/icons-react';
import { Box, NavLink } from '@mantine/core';
const data = [
  { icon: IconGauge, label: 'Dashboard', description: 'Item with description' },
  {
    icon: IconFingerprint,
    label: 'Security',
    rightSection: <IconChevronRight size={16} stroke={1.5} />,
  },
  { icon: IconActivity, label: 'Activity' },
];

function Demo() {
  const [active, setActive] = useStat
...
```

```python
import { NavLink } from '@mantine/core';

function Demo() {
  return (
    <>
      <NavLink color="lime.4" variant="filled" active label="Default" />
      <NavLink color="lime.4" variant="filled" active autoContrast label="Auto contrast" />
    </>
  );
}
```

---

## Notification | Mantine

**URL**: https://mantine.dev/core/notification/

**Contents**:
- Notification
- Usage
- With icon
- Styles API
- Accessibility

Show dynamic notifications and alerts to user, part of notifications system

Notification is a base component for notification system. Build your own or use @mantine/notifications package.

Notification supports Styles API, you can add styles to any inner element of the component withclassNames prop. Follow Styles API documentation to learn more.

Hover over selectors to highlight corresponding elements

Loader component, displayed only when `loading` prop is set

Icon component, displayed only when `icon` prop is set

Notification body, contains all other elements

Title element, displayed only when `title` prop is set

Description displayed below the title

To support screen readers, set close button aria-label or title with closeButtonProps:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { Notification } from '@mantine/core';

function Demo() {
  return (
    <Notification title="We notify you that">
      You are now obligated to give a star to Mantine project on GitHub
    </Notification>
  );
}
```

```python
import { IconX, IconCheck } from '@tabler/icons-react';
import { Notification } from '@mantine/core';

function Demo() {
  const xIcon = <IconX size={20} />;
  const checkIcon = <IconCheck size={20} />;

  return (
    <>
      <Notification icon={xIcon} color="red" title="Bummer!">
        Something went wrong
      </Notification>
      <Notification icon={checkIcon} color="teal" title="All good!" mt="md">
        Everything is fine
      </Notification>
    </>
  );
}
```

```text
/*
 * Hover over selectors to apply outline styles
 *
 */
```

---

## NumberInput | Mantine

**URL**: https://mantine.dev/core/number-input/

**Contents**:
- NumberInput
- Usage
- Controlled
- Value type
- min and max
- Clamp behavior
- Prefix and suffix
- Negative numbers

Capture number from user

NumberInput is based on react-number-format. It supports most of the props from the NumericFormat component in the original package.

NumberInput component supports Input and Input.Wrapper components features and all input element props. NumberInput documentation does not include all features supported by the component – see Input documentation to learn about all available features.

value, defaultValue and onChange props can be either string or number. In all cases when NumberInput value can be represented as a number, onChange function is called with a number (for example 55, 1.28, -100, etc.). But there are several cases when it is not possible to represent value as a number:

Set min and max props to limit the input value:

By default, the value is clamped when the input is blurred. If you set clampBehavior="strict", it will not be possible to enter value outside of min/max range. Note that this option may cause issues if you have tight min and max, for example min={10} and max={20}. If you need to disable value clamping entirely, set clampBehavior="none".

Set prefix and suffix props to add given string to the start or end of the input value:

By default, negative numbers are allowed. Set allowNegative={false} to allow only positive numbers.

By default, decimal numbers are allowed. Set allowDecimal={false} to allow only integers.

decimalScale controls how many decimal places are allowed:

Set fixedDecimalScale to always display fixed number of decimal places:

Set decimalSeparator to change decimal separator character:

Set thousandSeparator prop to separate thousands with a character. You can control grouping logic with thousandsGroupStyle, it accepts: thousand, lakh, wan, none values.

NumberInput supports leftSection and rightSection props. These sections are rendered with absolute position inside the input wrapper. You can use them to display icons, input controls or any other elements.

You can use the following props to control

*[Content truncated - see full docs]*

**Examples**:

```python
import { NumberInput } from '@mantine/core';

function Demo() {
  return (
    <NumberInput
      label="Input label"
      description="Input description"
      placeholder="Input placeholder"
    />
  );
}
```

```python
import { useState } from 'react';
import { NumberInput } from '@mantine/core';

function Demo() {
  const [value, setValue] = useState<string | number>('');
  return <NumberInput value={value} onChange={setValue} />;
}
```

```python
import { NumberInput } from '@mantine/core';

function Demo() {
  return (
    <NumberInput
      label="Enter value between 10 and 20"
      placeholder="Don't enter more than 20 and less than 10"
      min={10}
      max={20}
    />
  );
}
```

---

## Overlay | Mantine

**URL**: https://mantine.dev/core/overlay/

**Contents**:
- Overlay
- Usage
- Gradient
- Blur
- Polymorphic component

Overlays parent element with div element with any color and opacity

Overlay takes 100% of width and height of parent container or viewport if fixed prop is set. Set color and backgroundOpacity props to change Overlay background-color. Note that backgroundOpacity prop does not change CSS opacity property, it changes background-color. For example, if you set color="#000" and backgroundOpacity={0.85} background-color will be rgba(0, 0, 0, 0.85):

Set gradient prop to use background-image instead of background-color. When gradient prop is set, color and backgroundOpacity props are ignored.

Set blur prop to add backdrop-filter: blur({value}) styles. Note that backdrop-filter is not supported in all browsers.

Overlay is a polymorphic component – its default root element is div, but it can be changed to any other element or component with component prop:

You can also use components in component prop, for example, Next.js Link:

Polymorphic components with TypeScript

Note that polymorphic components props types are different from regular components – they do not extend HTML element props of the default element. For example, OverlayProps does not extend React.ComponentPropsWithoutRef'<'div'>' although div is the default element.

If you want to create a wrapper for a polymorphic component that is not polymorphic (does not support component prop), then your component props interface should extend HTML element props, for example:

If you want your component to remain polymorphic after wrapping, use createPolymorphicComponent function described in this guide.

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { useState } from 'react';
import { Button, Overlay, AspectRatio } from '@mantine/core';

function Demo() {
  const [visible, setVisible] = useState(true);
  return (
    <>
      <AspectRatio ratio={16 / 9} maw={400} mx="auto" pos="relative">
        <img
          src="https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/images/bg-1.png"
          alt="Demo"
        />
        {visible && <Overlay color="#000" backgroundOpacity={0.85} />}
      </AspectRatio>
      <Button 
...
```

```python
import { useState } from 'react';
import { Button, Overlay, AspectRatio } from '@mantine/core';

function Demo() {
  const [visible, setVisible] = useState(true);
  return (
    <>
      <AspectRatio ratio={16 / 9} maw={400} mx="auto" pos="relative">
        <img
          src="https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/images/bg-7.png"
          alt="Demo"
        />
        {visible && (
          <Overlay
            gradient="linear-gradient(145deg, rgba(0, 0, 0, 0.95)
...
```

```python
import { Overlay, AspectRatio } from '@mantine/core';

function Demo() {
  return (
    <AspectRatio ratio={16 / 9} maw={400} mx="auto" pos="relative">
      <img
        src="https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/images/bg-3.png"
        alt="Demo"
      />
      <Overlay color="#000" backgroundOpacity={0.35} blur={15} />
    </AspectRatio>
  );
}
```

---

## Pagination | Mantine

**URL**: https://mantine.dev/core/pagination/

**Contents**:
- Pagination
- Usage
- Example with chunked content
- Controlled
- Siblings
- Boundaries
- Hide pages controls
- Styles API

Display active page and navigate between multiple pages

id: 0, name: mantine-qz271msvj

id: 1, name: mantine-jsl64pzv5

id: 2, name: mantine-ox8ymw70w

id: 3, name: mantine-7cakj6yke

id: 4, name: mantine-5lkwdsoq6

To control component state provide value and onChange props:

Control number of active item siblings with siblings prop:

Control number of items displayed after previous and before next buttons with boundaries prop:

Set withPages={false} to hide pages controls:

Showing 1 – 10 of 145

Pagination supports Styles API, you can add styles to any inner element of the component withclassNames prop. Follow Styles API documentation to learn more.

Hover over selectors to highlight corresponding elements

Control element: items, next/previous, first/last buttons

You can use the following compound components to have full control over the Pagination rendering:

Pagination supports autoContrast prop and theme.autoContrast. If autoContrast is set either on Pagination or on theme, content color will be adjusted to have sufficient contrast with the value specified in color prop.

Note that autoContrast feature works only if you use color prop to change background color.

If you need more flexibility @mantine/hooks package exports use-pagination hook, you can use it to create custom pagination components.

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { Pagination } from '@mantine/core';

function Demo() {
  return <Pagination total={10} />;
}
```

```python
import { useState } from 'react';
import { randomId } from '@mantine/hooks';
import { Pagination, Text } from '@mantine/core';

function chunk<T>(array: T[], size: number): T[][] {
  if (!array.length) {
    return [];
  }
  const head = array.slice(0, size);
  const tail = array.slice(size);
  return [head, ...chunk(tail, size)];
}

const data = chunk(
  Array(30)
    .fill(0)
    .map((_, index) => ({ id: index, name: randomId() })),
  5
);

function Demo() {
  const [activePage, setPage] = us
...
```

```python
import { useState } from 'react';
import { Pagination } from '@mantine/core';

function Demo() {
  const [activePage, setPage] = useState(1);
  return (
    <Pagination value={activePage} onChange={setPage} total={10} />
  );
}
```

---

## Paper | Mantine

**URL**: https://mantine.dev/core/paper/

**Contents**:
- Paper
- Usage
- Polymorphic component

Renders white or dark background depending on color scheme

Paper is the most basic ui component

Use it to create cards, dropdowns, modals and other components that require background with shadow

Paper is a polymorphic component – its default root element is div, but it can be changed to any other element or component with component prop:

You can also use components in component prop, for example, Next.js Link:

Polymorphic components with TypeScript

Note that polymorphic components props types are different from regular components – they do not extend HTML element props of the default element. For example, PaperProps does not extend React.ComponentPropsWithoutRef'<'div'>' although div is the default element.

If you want to create a wrapper for a polymorphic component that is not polymorphic (does not support component prop), then your component props interface should extend HTML element props, for example:

If you want your component to remain polymorphic after wrapping, use createPolymorphicComponent function described in this guide.

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { Text, Paper } from '@mantine/core';

function Demo() {
  return (
    <Paper shadow="xs" p="xl">
      <Text>Paper is the most basic ui component</Text>
      <Text>
        Use it to create cards, dropdowns, modals and other components that require background
        with shadow
      </Text>
    </Paper>
  );
}
```

```python
import { Paper } from '@mantine/core';

function Demo() {
  return <Paper component="button" />;
}
```

```python
import Link from 'next/link';
import { Paper } from '@mantine/core';

function Demo() {
  return <Paper component={Link} href="/" />;
}
```

---

## PillsInput | Mantine

**URL**: https://mantine.dev/core/pills-input/

**Contents**:
- PillsInput
- Usage
- Input props
- Searchable select example
- Accessibility

Base component for custom tags inputs and multi selects

PillsInput is a utility component that can be used to create custom tag inputs, multi selects and other similar components. By itself it does not include any logic, it only renders given children. Usually, PillsInput is used in combination with Pill component.

PillsInput component supports Input and Input.Wrapper components features and all div element props. PillsInput documentation does not include all features supported by the component – see Input documentation to learn about all available features.

Combine PillsInput with Combobox to create searchable multiselect:

If PillsInput is used without label prop, it will not be announced properly by screen reader:

Set aria-label on the PillsInput.Field component to make the input accessible. In this case label will not be visible, but screen reader will announce it:

If label prop is set, the input will be accessible it is not required to set aria-label:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { PillsInput, Pill } from '@mantine/core';

function Demo() {
  return (
    <PillsInput label="PillsInput">
      <Pill.Group>
        <Pill>React</Pill>
        <Pill>Vue</Pill>
        <Pill>Svelte</Pill>
        <PillsInput.Field placeholder="Enter tags" />
      </Pill.Group>
    </PillsInput>
  );
}
```

```python
import { PillsInput, Pill } from '@mantine/core';

function Demo() {
  return (
    <PillsInput
      label="Input label"
      description="Input description"
    >
      <Pill.Group>
        <Pill>React</Pill>
        <Pill>Vue</Pill>
        <Pill>Svelte</Pill>
        <PillsInput.Field placeholder="Enter tags" />
      </Pill.Group>
    </PillsInput>
  );
}
```

```python
import { useState } from 'react';
import { PillsInput, Pill, Combobox, CheckIcon, Group, useCombobox } from '@mantine/core';

const groceries = ['🍎 Apples', '🍌 Bananas', '🥦 Broccoli', '🥕 Carrots', '🍫 Chocolate'];

function Demo() {
  const combobox = useCombobox({
    onDropdownClose: () => combobox.resetSelectedOption(),
    onDropdownOpen: () => combobox.updateSelectedOptionIndex('active'),
  });

  const [search, setSearch] = useState('');
  const [value, setValue] = useState<string[]>([]);


...
```

---

## PinInput | Mantine

**URL**: https://mantine.dev/core/pin-input/

**Contents**:
- PinInput
- Usage
- Regex type
- One time code
- Styles API
- Accessibility

Capture pin code or one time password from the user

You can use regular expression to validate user input. Characters that do not match given expression will be disregarded. For example, to create a PinInput that will accept only numbers from 0 to 3, set type={/^[0-3]+/}:

Some operating systems expose the last received SMS code to be used by applications like your keyboard. If the current form input asks for this code, your keyboard adapts and proposes the code as keyboard-suggestion. Prop oneTimeCode makes your input setting autocomplete="one-time-code" which allows using that feature.

PinInput supports Styles API, you can add styles to any inner element of the component withclassNames prop. Follow Styles API documentation to learn more.

Hover over selectors to highlight corresponding elements

Inputs do not have associated labels, set aria-label to make component visible to the screen reader:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { PinInput } from '@mantine/core';

function Demo() {
  return <PinInput />
}
```

```python
import { PinInput } from '@mantine/core';

function Demo() {
  return <PinInput type={/^[0-3]*$/} inputType="tel" inputMode="numeric" />;
}
```

```python
import { PinInput } from '@mantine/core';

function OneTimeCodeInput() {
  return <PinInput oneTimeCode />;
}
```

---

## Polymorphic components | Mantine

**URL**: https://mantine.dev/guides/polymorphic/

**Contents**:
- Polymorphic components
- What is a polymorphic component
- renderRoot prop
- Polymorphic components as other React components
- Polymorphic components as Next.js Link
- Polymorphic components with generic components
- Polymorphic components with react-router NavLink
- Wrapping polymorphic components

A polymorphic component is a component which root element can be changed with component prop. All polymorphic components have a default element which is used when component prop is not provided. For example, the Button component default element is button and it can be changed to a or any other element or component:

renderRoot is an alternative to the component prop, which accepts a function that should return a React element. It is useful in cases when component prop cannot be used, for example, when the component that you want to pass to the component is generic (accepts type or infers it from props, for example <Link<'/'> />).

Example of using renderRoot prop, the result is the same as in the previous demo:

!important It is required to spread props argument into the root element. Otherwise there will be no styles and the component might not be accessible.

You can pass any other React component to component prop. For example, you can pass Link component from react-router-dom:

Next.js link does not work in the same way as other similar components in all Next.js versions.

With Next.js 12 and below:

With Next.js 13 and above:

You cannot pass generic components to component prop because it is not possible to infer generic types from the component prop. For example, you cannot pass typed Next.js Link to component prop because it is not possible to infer href type from the component prop. The component itself will work correctly, but you will have a TypeScript error.

To make generic components work with polymorphic components, use renderRoot prop instead of component:

react-router-dom NavLink component className prop accepts a function based on which you can add an active class to the link. This feature is incompatible with Mantine component prop, but you can use renderRoot prop instead:

Non-polymorphic components include React.ComponentPropsWithoutRef<'x'> as a part of their props type, where x is a root element of the component. For example, Container compon

*[Content truncated - see full docs]*

**Examples**:

```python
import { Button } from '@mantine/core';

function Demo() {
  return (
    <Button component="a" href="https://mantine.dev/" target="_blank">
      Mantine website
    </Button>
  );
}
```

```python
import { Button } from '@mantine/core';

function Demo() {
  return (
    <Button
      renderRoot={(props) => (
        <a href="https://mantine.dev/" target="_blank" {...props} />
      )}
    >
      Mantine website
    </Button>
  );
}
```

```python
import { Link } from 'react-router-dom';
import { Button } from '@mantine/core';

function Demo() {
  return (
    <Button component={Link} to="/react-router">
      React router link
    </Button>
  );
}
```

---

## Popover | Mantine

**URL**: https://mantine.dev/core/popover/

**Contents**:
- Popover
- Usage
- Controlled
- Focus trap
- Inline elements
- Same width
- offset
- Middlewares

Display popover section relative to given target element

You can control Popover state with opened and onChange props:

Controlled example with mouse events:

If you need to use interactive elements (inputs, buttons, etc.) inside Popover.Dropdown, set trapFocus prop:

Enable inline middleware to use Popover with inline elements:

Stantler’s magnificent antlers were traded at high prices as works of art. As a result, this Pokémon was hunted close to extinction by those who were after the priceless antlers. When visiting a junkyard, you may catch sight of it having an intense fight with Murkrow over shiny objects.Ho-Oh’s feathers glow in seven colors depending on the angle at which they are struck by light. These feathers are said to bring happiness to the bearers. This Pokémon is said to live at the foot of a rainbow.

Set width="target" prop to make Popover dropdown take the same width as target element:

Set offset prop to a number to change dropdown position relative to the target element. This way you can control dropdown offset on main axis only.

To control offset on both axis, pass object with mainAxis and crossAxis properties:

You can enable or disable Floating UI middlewares with middlewares prop:

Example of turning off shift and flip middlewares:

To customize Floating UI middlewares options, pass them as an object to the middlewares prop. For example, to change shift middleware padding to 20px use the following configuration:

Set withArrow prop to add an arrow to the dropdown. Arrow is a div element rotated with transform: rotate(45deg).

arrowPosition prop determines how arrow is position relative to the target element when position is set to *-start and *-end values on Popover component. By default, the value is center – the arrow is positioned in the center of the target element if it is possible.

If you change arrowPosition to side, then the arrow will be positioned on the side of the target element, and you will be able to control arrow offset wi

*[Content truncated - see full docs]*

**Examples**:

```python
import { Popover, Text, Button } from '@mantine/core';

function Demo() {
  return (
    <Popover width={200} position="bottom" withArrow shadow="md">
      <Popover.Target>
        <Button>Toggle popover</Button>
      </Popover.Target>
      <Popover.Dropdown>
        <Text size="xs">This is uncontrolled popover, it is opened when button is clicked</Text>
      </Popover.Dropdown>
    </Popover>
  );
}
```

```python
import { useState } from 'react';
import { Button, Popover } from '@mantine/core';

function Demo() {
  const [opened, setOpened] = useState(false);
  return (
    <Popover opened={opened} onChange={setOpened}>
      <Popover.Target>
        <Button onClick={() => setOpened((o) => !o)}>
          Toggle popover
        </Button>
      </Popover.Target>

      <Popover.Dropdown>Dropdown</Popover.Dropdown>
    </Popover>
  );
}
```

```python
import { useDisclosure } from '@mantine/hooks';
import { Popover, Text, Button } from '@mantine/core';

function Demo() {
  const [opened, { close, open }] = useDisclosure(false);
  return (
    <Popover width={200} position="bottom" withArrow shadow="md" opened={opened}>
      <Popover.Target>
        <Button onMouseEnter={open} onMouseLeave={close}>
          Hover to see popover
        </Button>
      </Popover.Target>
      <Popover.Dropdown style={{ pointerEvents: 'none' }}>
        <Text 
...
```

---

## Portal | Mantine

**URL**: https://mantine.dev/core/portal/

**Contents**:
- Portal
- Usage
- Reuse target node
- Specify target DOM node
- Server side rendering
- OptionalPortal component

Renders component outside of parent element tree

Portal is a wrapper component for ReactDOM.createPortal API. Render any component or element at the end of document.body or at a given element. Modal and Drawer components are wrapped in Portal by default.

Use Portal to render a component or an element at a different place (defaults to the end of document.body). Portal is useful when you want to prevent parent styles from interfering with children, usually all these styles are related to position and z-index properties and portals are used for components with fixed position, for example, modals.

In the example above, the div element is rendered outside of parent main (before closing body tag), but still receives opened and onClose props. The element will not be affected by parent z-index.

By default, Portal creates a new target node for each instance. To change this behavior and reuse the same target node for all instances, set reuseTargetNode prop. In the following example, all three paragraphs will be rendered in the same target node:

You can specify dom node where portal will be rendered by passing target prop:

Alternatively, you can specify selector to render portal in existing element:

If you don't specify the target element, new one will be created and appended to the document.body for each Portal component.

createPortal is not supported during server side rendering. All components inside Portal are rendered only after the application was mounted to the dom.

OptionalPortal component lets you configure whether children should be rendered in Portal. It accepts the same props as the Portal component:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { useState } from 'react';
import { Portal } from '@mantine/core';

function Demo() {
  const [opened, setOpened] = useState(false);

  return (
    <main style={{ position: 'relative', zIndex: 1 }}>
      {opened && (
        <Portal>
          <div>Your modal content</div>
        </Portal>
      )}

      <button onClick={() => setOpened(true)} type="button">
        Open modal
      </button>
    </main>
  );
}
```

```python
import { Portal } from '@mantine/core';

function Demo() {
  return (
    <>
      <Portal reuseTargetNode>
        <p>First</p>
      </Portal>

      <Portal reuseTargetNode>
        <p>Second</p>
      </Portal>

      <Portal reuseTargetNode>
        <p>Third</p>
      </Portal>
    </>
  );
}
```

```python
import { Portal } from '@mantine/core';

const container = document.createElement('div');
document.body.appendChild(container);

function Demo() {
  return <Portal target={container}>My portal</Portal>;
}
```

---

## Progress | Mantine

**URL**: https://mantine.dev/core/progress/

**Contents**:
- Progress
- Usage
- Compound components
- Vertical orientation
- With tooltips
- Section width transition
- Example: progress with segments
- Styles API

Give user feedback for status of the task

Set transitionDuration to a number of ms to enable width transition:

Progress supports Styles API, you can add styles to any inner element of the component withclassNames prop. Follow Styles API documentation to learn more.

Hover over selectors to highlight corresponding elements

`Progress.Section` root element

`Progress.Label` root element

Set aria-label attribute to label progress:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { Progress } from '@mantine/core';

function Demo() {
  return <Progress value={50} />;
}
```

```python
import { Progress } from '@mantine/core';

function Demo() {
  return (
    <Progress.Root size="xl">
      <Progress.Section value={35} color="cyan">
        <Progress.Label>Documents</Progress.Label>
      </Progress.Section>
      <Progress.Section value={28} color="pink">
        <Progress.Label>Photos</Progress.Label>
      </Progress.Section>
      <Progress.Section value={15} color="orange">
        <Progress.Label>Other</Progress.Label>
      </Progress.Section>
    </Progress.Root>
  );
...
```

```python
import { Progress } from '@mantine/core';

function Demo() {
  return (
    <Group>
      <Progress value={80} orientation="vertical" h={200} />
      <Progress value={60} color="orange" size="xl" orientation="vertical" h={200} animated />

      <Progress.Root size="xl" autoContrast orientation="vertical" h={200}>
        <Progress.Section value={40} color="lime.4">
          <Progress.Label>Documents</Progress.Label>
        </Progress.Section>
        <Progress.Section value={20} color="yello
...
```

---

## Radio | Mantine

**URL**: https://mantine.dev/core/radio/

**Contents**:
- Radio
- Usage
- Controlled
- States
- Change icon
- Change icon color
- Disabled state
- Pointer cursor

Wrapper for input type radio

By default, radio input and label have cursor: default (same as native input[type="radio"]). To change cursor to pointer, set cursorType on theme:

You can change target element to which tooltip is attached with refProp:

All props passed to the component are forwarded to the input element. If you need to add props to the root element, use wrapperProps. In the following example:

Radio.Indicator looks exactly the same as Radio component, but it does not have any semantic meaning, it's just a visual representation of radio state. You can use it in any place where you need to display radio state without any interaction related to the indicator. For example, it is useful in cards based on buttons, trees, etc.

Note that Radio.Indicator cannot be focused or selected with keyboard. It is not accessible and should not be used as a replacement for Radio component.

Radio.Card component can be used as a replacement for Radio to build custom cards/buttons/other things that work as radios. The root element of the component has role="radio" attribute, it is accessible by default and supports the same keyboard interactions as input[type="radio"].

Core components library: inputs, buttons, overlays, etc.

You can use Radio.Card with Radio.Group the same way as Radio component:

Choose a package that you will need in your application

Core components library: inputs, buttons, overlays, etc.

Collection of reusable hooks for React applications.

@mantine/notifications

Radio supports Styles API, you can add styles to any inner element of the component withclassNames prop. Follow Styles API documentation to learn more.

Hover over selectors to highlight corresponding elements

Input element (`input[type="radio"]`)

Radio icon, used to display checked icon

Wrapper for `icon` and `input`

Input body, contains all other elements

Contains `label`, `description` and `error`

Description displayed below the label

Error message displayed below the label

S

*[Content truncated - see full docs]*

**Examples**:

```python
import { Radio } from '@mantine/core';

function Demo() {
  return (
    <Radio
      label="I cannot be unchecked"
    />
  );
}
```

```python
import { useState } from 'react';
import { Radio } from '@mantine/core';

function Demo() {
  const [checked, setChecked] = useState(false);
  return (
    <Radio
      checked={checked}
      onChange={(event) => setChecked(event.currentTarget.checked)}
    />
  );
}
```

```python
import { Radio, Stack } from '@mantine/core';

function Demo() {
  return (
    <Stack>
      <Radio checked={false} onChange={() => {}} label="Default radio" />
      <Radio checked onChange={() => {}} label="Checked radio" />
      <Radio checked variant="outline" onChange={() => {}} label="Outline checked radio" />
      <Radio disabled label="Disabled radio" />
      <Radio disabled checked onChange={() => {}} label="Disabled checked radio" />
    </Stack>
  );
}
```

---

## RangeSlider | Mantine

**URL**: https://mantine.dev/core/range-slider/

**Contents**:
- RangeSlider
- Usage
- Controlled
- Disabled
- Control label
- Min, max and step
- Domain
- Decimal values

RangeSlider component

To change label behavior and appearance, set the following props:

Custom label transition

Step matched with marks

By default, min and max values define the possible range of values. domain prop allows setting the possible range of values independently of the min and max values:

To use RangeSlider with decimal values, set min, max and step props:

Use minRange prop to control minimum range between from and to values in RangeSlider. The default value is 10. The example below shows how to use minRange prop to capture decimal values from the user:

pushOnOverlap prop controls whether the thumbs should push each other when they overlap. By default, pushOnOverlap is true, if you want to disable this behavior, set it to false.

Example of pushOnOverlap={false}:

Add any number of marks to slider by setting marks prop to an array of objects:

Note that mark value is relative to slider value, not width:

Set restrictToMarks prop to restrict slider value to marks only. Note that in this case step prop is ignored:

You can invert the track with the inverted prop:

RangeSlider component is accessible by default:

To label component for screen readers, add labels to thumbs:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { RangeSlider } from '@mantine/core';

function Demo() {
  return (
    <RangeSlider
      color="blue"
      defaultValue={[20, 60]}
      marks={[
        { value: 20, label: '20%' },
        { value: 50, label: '50%' },
        { value: 80, label: '80%' },
      ]}
    />
  );
}
```

```python
import { useState } from 'react';
import { RangeSlider } from '@mantine/core';

function Demo() {
  const [value, setValue] = useState<[number, number]>([20, 80]);
  return <RangeSlider value={value} onChange={setValue} />;
}
```

```python
import { RangeSlider } from '@mantine/core';

function Demo() {
  return <RangeSlider defaultValue={[20, 60]} disabled />;
}
```

---

## Rating | Mantine

**URL**: https://mantine.dev/core/rating/

**Contents**:
- Rating
- Usage
- Controlled
- Read only
- Fractions
- Custom symbol
- Symbols for each item

Pick and display rating

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { Rating } from '@mantine/core';

function Demo() {
  return <Rating defaultValue={2} />
}
```

```python
import { useState } from 'react';
import { Rating } from '@mantine/core';

function Demo() {
  const [value, setValue] = useState(0);
  return <Rating value={value} onChange={setValue} />;
}
```

```python
import { Rating } from '@mantine/core';

function Demo() {
  return <Rating value={3.5} fractions={2} readOnly />;
}
```

---

## RingProgress | Mantine

**URL**: https://mantine.dev/core/ring-progress/

**Contents**:
- RingProgress
- Usage
- Size, thickness & rounded caps
- Sections tooltips
- Root color
- Sections props
- Customize label
- Filled segment transition

Give user feedback for status of the task with circle diagram

Set sections prop to an array of:

Application data usage

Use size, thickness & roundCaps props to configure RingProgress, size and thickness values:

Add tooltip property to section to display floating Tooltip when user hovers over it:

Hover sections to see tooltips

Use rootColor property to change the root color:

You can add any additional props to sections:

Hovered section: none

You can add any React node as label, for example Text component with some additional styles or ThemeIcon:

By default, transitions are disabled, to enable them, set transitionDuration prop to a number of milliseconds:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { RingProgress, Text } from '@mantine/core';

function Demo() {
  return (
    <RingProgress
      label={
        <Text size="xs" ta="center">
          Application data usage
        </Text>
      }
      sections={[
        { value: 40, color: 'cyan' },
        { value: 15, color: 'orange' },
        { value: 15, color: 'grape' },
      ]}
    />
  );
}
```

```python
import { RingProgress } from '@mantine/core';
function Demo() {
  return (
    <RingProgress
      size={120}
      thickness={12}
      roundCaps
      sections={[
        { value: 40, color: 'cyan' },
        { value: 15, color: 'orange' },
        { value: 15, color: 'grape' },
      ]}
    />
  )
}
```

```python
import { RingProgress, Text } from '@mantine/core';

function Demo() {
  return (
    <RingProgress
      size={170}
      thickness={16}
      label={
        <Text size="xs" ta="center" px="xs" style={{ pointerEvents: 'none' }}>
          Hover sections to see tooltips
        </Text>
      }
      sections={[
        { value: 40, color: 'cyan', tooltip: 'Documents – 40 Gb' },
        { value: 25, color: 'orange', tooltip: 'Apps – 25 Gb' },
        { value: 15, color: 'grape', tooltip: 'Other 
...
```

---

## ScrollArea | Mantine

**URL**: https://mantine.dev/core/scroll-area/

**Contents**:
- ScrollArea
- Usage
- Horizontal scrollbars
- Disable horizontal scrollbars
- Subscribe to scroll position changes
- Scroll to position
- Styles API
- Scroll element into view

Area with custom scrollbars

ScrollArea component supports the following props:

Charizard description from Bulbapedia

Charizard is a draconic, bipedal Pokémon. It is primarily orange with a cream underside from the chest to the tip of its tail. It has a long neck, small blue eyes, slightly raised nostrils, and two horn-like structures protruding from the back of its rectangular head. There are two fangs visible in the upper jaw when its mouth is closed. Two large wings with blue-green undersides sprout from its back, and a horn-like appendage juts out from the top of the third joint of each wing. A single wing-finger is visible through the center of each wing membrane. Charizard's arms are short and skinny compared to its robust belly, and each limb has three white claws. It has stocky legs with cream-colored soles on each of its plantigrade feet. The tip of its long, tapering tail burns with a sizable flame.

As Mega Charizard X, its body and legs are more physically fit, though its arms remain thin. Its skin turns black with a sky-blue underside and soles. Two spikes with blue tips curve upward from the front and back of each shoulder, while the tips of its horns sharpen, turn blue, and curve slightly upward. Its brow and claws are larger, and its eyes are now red. It has two small, fin-like spikes under each horn and two more down its lower neck. The finger disappears from the wing membrane, and the lower edges are divided into large, rounded points. The third joint of each wing-arm is adorned with a claw-like spike. Mega Charizard X breathes blue flames out the sides of its mouth, and the flame on its tail now burns blue. It is said that its new power turns it black and creates more intense flames.

Charizard description from Bulbapedia

Charizard is a draconic, bipedal Pokémon. It is primarily orange with a cream underside from the chest to the tip of its tail. It has a long neck, small blue eyes, slightly raised nostrils, and two horn-like structures protrud

*[Content truncated - see full docs]*

**Examples**:

```python
import { ScrollArea } from '@mantine/core';

function Demo() {
  return (
    <ScrollArea h={250}>
      {/* ... content */}
    </ScrollArea>
  );
}
```

```python
import { ScrollArea, Box } from '@mantine/core';

function Demo() {
  return (
    <ScrollArea w={300} h={200}>
      <Box w={600}>
        {/* ... content */}
      </Box>
    </ScrollArea>
  );
}
```

```python
import { ScrollArea, Box } from '@mantine/core';

function Demo() {
  return (
    <ScrollArea w={300} h={200} scrollbars="y">
      <Box w={600}>
        {/* ... content */}
      </Box>
    </ScrollArea>
  );
}
```

---

## SegmentedControl | Mantine

**URL**: https://mantine.dev/core/segmented-control/

**Contents**:
- SegmentedControl
- Usage
- Controlled
- Data prop
- Disabled
- React node as label
- Color
- Transitions

A linear set of two or more segments

SegmentedControl support two different data formats:

To disable SegmentedControl item, use array of objects data format and set disabled: true on the item that you want to disable. To disable the entire component, use disabled prop.

You can use any React node as label:

By default, SegmentedControl uses theme.white with shadow in light color scheme and var(--mantine-color-dark-6) background color for indicator. Set color prop to change indicator background-color:

Change transition properties with:

500ms linear transition

Set readOnly prop to prevent value from being changed:

SegmentedControl supports Styles API, you can add styles to any inner element of the component withclassNames prop. Follow Styles API documentation to learn more.

Hover over selectors to highlight corresponding elements

Wrapper element for input and label

Input element (`input[type="radio"]`), hidden by default

Label element associated with input

Floating indicator that moves between items

Wrapper of label element children

SegmentedControl uses radio inputs under the hood, it is accessible by default with no extra steps required if you have text in labels. Component support the same keyboard events as a regular radio group.

In case you do not have text in labels (for example, when you want to use SegmentedControl with icons only), use VisuallyHidden to make component accessible:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { SegmentedControl } from '@mantine/core';

function Demo() {
  return <SegmentedControl data={['React', 'Angular', 'Vue']} />;
}
```

```python
import { useState } from 'react';
import { SegmentedControl } from '@mantine/core';

function Demo() {
  const [value, setValue] = useState('react');

  return (
    <SegmentedControl
      value={value}
      onChange={setValue}
      data={[
        { label: 'React', value: 'react' },
        { label: 'Angular', value: 'ng' },
        { label: 'Vue', value: 'vue' },
        { label: 'Svelte', value: 'svelte' },
      ]}
    />
  );
}
```

```python
import { SegmentedControl } from '@mantine/core';

function ArrayOfStrings() {
  return (
    <SegmentedControl data={['React', 'Angular', 'Svelte', 'Vue']} />
  );
}

function ArrayOfObjects() {
  return (
    <SegmentedControl
      data={[
        { value: 'React', label: 'React' },
        { value: 'Angular', label: 'Angular' },
        { value: 'Svelte', label: 'Svelte' },
        { value: 'Vue', label: 'Vue' },
      ]}
    />
  );
}
```

---

## Select | Mantine

**URL**: https://mantine.dev/core/select/

**Contents**:
- Select
- Made with Combobox
- Usage
- Controlled
- onChange handler
- autoSelectOnBlur
- Clearable
- Allow deselect

Custom searchable select

Select is an opinionated component built on top of Combobox component. It has a limited set of features to cover only the basic use cases. If you need more advanced features, you can build your own component with Combobox. You can find examples of custom select components on the examples page.

Select allows capturing user input based on suggestions from the list. Unlike Autocomplete, Select does not allow entering custom values.

Select value must be a string, other types are not supported. onChange function is called with a string value as a single argument.

onChange is called with two arguments:

If you prefer object format in state, use second argument of onChange handler:

Set autoSelectOnBlur prop to automatically select the highlighted option when the input loses focus. To see this feature in action: select an option with up/down arrows, then click outside the input:

Set clearable prop to display the clear button in the right section. The button is not displayed when:

allowDeselect prop determines whether the value should be deselected when user clicks on the selected option. By default, allowDeselect is true:

This is default behavior, click 'React' in the dropdown

Set searchable prop to allow filtering options by user input:

You can control search value with searchValue and onSearchChange props:

Set the nothingFoundMessage prop to display a given message when no options match the search query or there is no data available. If the nothingFoundMessage prop is not set, the Select dropdown will be hidden.

Set checkIconPosition prop to left or right to control position of check icon in active option. To remove the check icon, set withCheckIcon={false}.

Select data prop accepts data in one of the following formats:

Array of object with value, label and optional disabled keys:

Array of groups with string options:

Array of groups with object options:

Example of a custom filter function that matches options by words instead of l

*[Content truncated - see full docs]*

**Examples**:

```python
import { Select } from '@mantine/core';

function Demo() {
  return (
    <Select
      label="Your favorite library"
      placeholder="Pick value"
      data={['React', 'Angular', 'Vue', 'Svelte']}
    />
  );
}
```

```python
import { useState } from 'react';
import { Select } from '@mantine/core';

function Demo() {
  const [value, setValue] = useState<string | null>('');
  return <Select data={[]} value={value} onChange={setValue} />;
}
```

```python
import { useState } from 'react';
import { ComboboxItem, Select } from '@mantine/core';

function Demo() {
  const [value, setValue] = useState<ComboboxItem | null>(null);
  return (
    <Select
      data={[{ value: 'react', label: 'React library' }]}
      value={value ? value.value : null}
      onChange={(_value, option) => setValue(option)}
    />
  );
}
```

---

## SimpleGrid | Mantine

**URL**: https://mantine.dev/core/simple-grid/

**Contents**:
- SimpleGrid
- Usage
- spacing and verticalSpacing props
- Responsive props
- Container queries
- Browser support

Responsive grid in which each item takes equal amount of space

SimpleGrid is a responsive grid system with equal-width columns. It uses CSS grid layout. If you need to set different widths for columns, use Grid component instead.

spacing prop is used both for horizontal and vertical spacing if verticalSpacing is not set:

cols, spacing and verticalSpacing props support object notation for responsive values, it works the same way as style props: the object may have base, xs, sm, md, lg and xl key, and values from those keys will be applied according to current viewport width.

In the following example, cols={{ base: 1, sm: 2, lg: 5 }} means:

Same logic applies to spacing and verticalSpacing props.

To use container queries instead of media queries, set type="container". With container queries, grid columns and spacing will be adjusted based on the container width, not the viewport width.

Note that, when using container queries, cols, spacing and verticalSpacing props cannot reference theme.breakpoints values in keys. It is required to use exact px or em values.

To see how the grid changes, resize the root element of the demo with the resize handle located at the bottom right corner of the demo:

SimpleGrid uses CSS Grid Layout, it is supported in all modern browsers. If you need to support older browsers, use Grid (flexbox based) component instead.

When type="container" is set, SimpleGrid uses container queries. Since February 2023, container queries are supported in all modern browsers. If you need to support older browsers, do not use container queries option.

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { SimpleGrid } from '@mantine/core';

function Demo() {
  return (
    <SimpleGrid cols={3}>
      <div>1</div>
      <div>2</div>
      <div>3</div>
      <div>4</div>
      <div>5</div>
    </SimpleGrid>
  )
}
```

```python
import { SimpleGrid } from '@mantine/core';

// `spacing` is used for both horizontal and vertical spacing
const Spacing = () => <SimpleGrid spacing="xl" />;

// `spacing` is used for horizontal spacing, `verticalSpacing` for vertical
const VerticalSpacing = () => (
  <SimpleGrid spacing="xl" verticalSpacing="lg" />
);
```

```python
import { SimpleGrid } from '@mantine/core';

function Demo() {
  return (
    <SimpleGrid
      cols={{ base: 1, sm: 2, lg: 5 }}
      spacing={{ base: 10, sm: 'xl' }}
      verticalSpacing={{ base: 'md', sm: 'xl' }}
    >
      <div>1</div>
      <div>2</div>
      <div>3</div>
      <div>4</div>
      <div>5</div>
    </SimpleGrid>
  );
}
```

---

## Slider | Mantine

**URL**: https://mantine.dev/core/slider/

**Contents**:
- Slider
- Usage
- Controlled
- Disabled
- onChangeEnd
- Control label
- Min, max and step
- Domain

onChangeEnd callback is called when user the slider is stopped from being dragged or value is changed with keyboard. You can use it as a debounced callback to avoid too frequent updates.

onChangeEnd value: 50

To change label behavior and appearance, set the following props:

Custom label transition

Step matched with marks

By default, min and max values define the possible range of values. domain prop allows setting the possible range of values independently of the min and max values:

To use Slider with decimal values, set min, max and step props:

Add any number of marks to slider by setting marks prop to an array of objects:

Note that mark value is relative to slider value, not width:

Set restrictToMarks prop to restrict slider value to marks only. Note that in this case step prop is ignored:

You can use the scale prop to represent the value on a different scale.

In the following demo, the value x represents the value 2^x. Increasing x by one increases the represented value by 2 to the power of x.

You can invert the track with the inverted prop:

Slider supports Styles API, you can add styles to any inner element of the component withclassNames prop. Follow Styles API documentation to learn more.

Hover over selectors to highlight corresponding elements

Contains `mark` and `markLabel` elements

Mark displayed on track

Label of the associated mark, displayed below track

Example of using Styles API to change Slider styles:

Slider does not provide vertical orientation as it is very rarely used. If you need this feature you can build it yourself with use-move hook.

If Slider component does not meet your requirements, you can build a custom slider with use-move hook:

Slider component is accessible by default:

To label component for screen readers, add labels to thumbs:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { Slider } from '@mantine/core';

function Demo() {
  return (
    <Slider
      color="blue"
      defaultValue={40}
      marks={[
        { value: 20, label: '20%' },
        { value: 50, label: '50%' },
        { value: 80, label: '80%' },
      ]}
    />
  );
}
```

```python
import { useState } from 'react';
import { Slider } from '@mantine/core';

function Demo() {
  const [value, setValue] = useState(40);
  return <Slider value={value} onChange={setValue} />;
}
```

```python
import { Slider } from '@mantine/core';

function Demo() {
  return <Slider defaultValue={60} disabled />;
}
```

---

## Spoiler | Mantine

**URL**: https://mantine.dev/core/spoiler/

**Contents**:
- Spoiler
- Usage
- Control expanded state
- Subscribe to expanded state changes
- Transition duration
- Get control ref

Hide long sections of content under a spoiler

Use Spoiler to hide long section of content. Set maxHeight prop to control point at which content will be hidden under spoiler and show/hide control appears. If the content height is less than maxHeight, the spoiler will just render children.

hideLabel and showLabel props are required – they are used as spoiler toggle button label in corresponding state.

We Butter the Bread with Butter was founded in 2007 by Marcel Neumann, who was originally guitarist for Martin Kesici's band, and Tobias Schultka. The band was originally meant as a joke, but progressed into being a more serious musical duo. The name for the band has no particular meaning, although its origins were suggested from when the two original members were driving in a car operated by Marcel Neumann and an accident almost occurred. Neumann found Schultka "so funny that he briefly lost control of the vehicle." Many of their songs from this point were covers of German folk tales and nursery rhymes.

To control expanded state use expanded and onExpandedChange props. Note that expanded prop does not have any effect on spoiler visuals if the content height is less than given maxHeight.

Use onExpandedChange to subscribe to expanded state changes:

Control transition duration by setting transitionDuration prop (transition-duration CSS property in ms). To disable animations, set transitionDuration={0}:

We Butter the Bread with Butter was founded in 2007 by Marcel Neumann, who was originally guitarist for Martin Kesici's band, and Tobias Schultka. The band was originally meant as a joke, but progressed into being a more serious musical duo. The name for the band has no particular meaning, although its origins were suggested from when the two original members were driving in a car operated by Marcel Neumann and an accident almost occurred. Neumann found Schultka "so funny that he briefly lost control of the vehicle." Many of their songs from this point were covers of 

*[Content truncated - see full docs]*

**Examples**:

```python
import { Spoiler } from '@mantine/core';

function Demo() {
  return (
    <Spoiler maxHeight={120} showLabel="Show more" hideLabel="Hide">
      {/* Content here */}
    </Spoiler>
  );
}
```

```python
import { useState } from 'react';
import { Spoiler } from '@mantine/core';

function Demo() {
  const [expanded, setExpanded] = useState(false);

  return (
    <Spoiler
      showLabel="Show more"
      hideLabel="Hide details"
      expanded={expanded}
      onExpandedChange={setExpanded}
    >
      {/* Spoiler content */}
    </Spoiler>
  );
}
```

```python
import { Spoiler } from '@mantine/core';

function Demo() {
  return (
    <Spoiler
      showLabel="Show more"
      hideLabel="Hide details"
      onExpandedChange={(expanded) => console.log(expanded)}
    >
      {/* Spoiler content */}
    </Spoiler>
  );
}
```

---

## Stepper | Mantine

**URL**: https://mantine.dev/core/stepper/

**Contents**:
- Stepper
- Usage
- Allow step select
- Disable next steps selection
- Color, radius and size
- With custom icons
- Vertical orientation
- Icon position

Display content divided into a steps sequence

To disable step selection, set allowStepSelect prop on Stepper.Step component. It can be used to prevent the user from reaching next steps while letting them go back and forth between steps they've already reached before:

Another way to disable selection of upcoming steps is to use the allowNextStepsSelect directly on the Stepper component. This is useful when you don't need to control the behavior specifically for each step.

Component size is controlled by two props: size and iconSize. size prop controls icon size, label and description font size. iconSize allows to overwrite icon size separately from other size values:

You can replace the step icon by setting icon prop on Stepper.Step component. To change completed check icon set completedIcon on Stepper component. You can use any React node as an icon: component, string, number:

You can use Stepper with icons only. Note that in this case, you will have to set aria-label or title on Stepper.Step component to make it accessible:

You can also change the completed icon for each step, for example, to indicate error state:

To change step icon and body arrangement, set iconPosition="right":

To indicate loading state set loading prop on Step component, Loader will replace step icon. You can configure the default loader in the theme.

Stepper supports Styles API, you can add styles to any inner element of the component withclassNames prop. Follow Styles API documentation to learn more.

Hover over selectors to highlight corresponding elements

Steps controls wrapper

Separator line between step controls

Vertical separator line between step controls

Current step content wrapper

Wrapper for the step icon and separator

Completed step icon, rendered within stepIcon

Contains stepLabel and stepDescription

Examples of styles customization with Styles API:

You can get refs of step button and stepper root element (div):

Stepper component relies on Stepper.Step order. Wr

*[Content truncated - see full docs]*

**Examples**:

```python
import { useState } from 'react';
import { Stepper, Button, Group } from '@mantine/core';

function Demo() {
  const [active, setActive] = useState(1);
  const nextStep = () => setActive((current) => (current < 3 ? current + 1 : current));
  const prevStep = () => setActive((current) => (current > 0 ? current - 1 : current));

  return (
    <>
      <Stepper active={active} onStepClick={setActive}>
        <Stepper.Step label="First step" description="Create an account">
          Step 1 conten
...
```

```python
import { useState } from 'react';
import { Stepper, Button, Group } from '@mantine/core';

function Demo() {
  const [active, setActive] = useState(1);
  const [highestStepVisited, setHighestStepVisited] = useState(active);

  const handleStepChange = (nextStep: number) => {
    const isOutOfBounds = nextStep > 3 || nextStep < 0;

    if (isOutOfBounds) {
      return;
    }

    setActive(nextStep);
    setHighestStepVisited((hSC) => Math.max(hSC, nextStep));
  };

  // Allow the user to freely
...
```

```python
import { useState } from 'react';
import { Stepper, Button, Group } from '@mantine/core';

function Demo() {
  const [active, setActive] = useState(1);
  const nextStep = () => setActive((current) => (current < 3 ? current + 1 : current));
  const prevStep = () => setActive((current) => (current > 0 ? current - 1 : current));

  return (
    <>
      <Stepper active={active} onStepClick={setActive} allowNextStepsSelect={false}>
        <Stepper.Step label="First step" description="Create an acco
...
```

---

## Switch | Mantine

**URL**: https://mantine.dev/core/switch/

**Contents**:
- Switch
- Usage
- Controlled
- Inner Labels
- Icon labels
- Thumb icon
- With tooltip
- Pointer cursor

Capture boolean input from user

Set refProp="rootRef" on Tooltip and other similar components to make them work with Switch:

By default, switch input and label have cursor: default (same as native input[type="checkbox"]). To change cursor to pointer, set cursorType on theme:

All props passed to the component are forwarded to the input element. If you need to add props to the root element, use wrapperProps. In the following example:

Switch supports Styles API, you can add styles to any inner element of the component withclassNames prop. Follow Styles API documentation to learn more.

Hover over selectors to highlight corresponding elements

Switch track, contains `thumb` and `trackLabel`

Label displayed inside `track`

Thumb displayed inside `track`

Input element (`input[type="checkbox"]`), hidden by default

Input body, contains all other elements

Contains `label`, `description` and `error`

Description displayed below the label

Error message displayed below the label

Switch is a regular input[type="checkbox"]. Set aria-label if the Switch is used without label prop:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { Switch } from '@mantine/core';

function Demo() {
  return (
    <Switch
      defaultChecked
      label="I agree to sell my privacy"
    />
  );
}
```

```python
import { useState } from 'react';
import { Switch } from '@mantine/core';

function Demo() {
  const [checked, setChecked] = useState(false);
  return (
    <Switch
      checked={checked}
      onChange={(event) => setChecked(event.currentTarget.checked)}
    />
  );
}
```

```python
import { Switch, Group } from '@mantine/core';

function Demo() {
  return (
    <Group justify="center">
      <Switch size="xs" onLabel="ON" offLabel="OFF" />
      <Switch size="sm" onLabel="ON" offLabel="OFF" />
      <Switch size="md" onLabel="ON" offLabel="OFF" />
      <Switch size="lg" onLabel="ON" offLabel="OFF" />
      <Switch size="xl" onLabel="ON" offLabel="OFF" />
    </Group>
  );
}
```

---

## TableOfContents | Mantine

**URL**: https://mantine.dev/core/table-of-contents/

**Contents**:
- TableOfContents
- Usage
- use-scroll-spy options
- Pass props to controls
- Initial data
- Depth offset
- autoContrast
- Styles API

Renders a list of headings on the page and tracks current heading visible in the viewport

Use TableOfContents component to display table of contents like in the sidebar of mantine.dev documentation. The component tracks scroll position and highlights current heading in the list.

TableOfContents in based on use-scroll-spy hook. You can pass options down to use-scroll-spy hook using scrollSpyOptions prop.

Example of customizing selector, depth and value retrieval:

You can pass props down to controls rendered by TableOfContents component with getControlProps function. It accepts an object with active and data properties and should return props object.

Example of changing controls to links:

TableOfContents retrieves data on mount. If you want to render headings before TableOfContents component is mounted (for example during server-side rendering), you can pass initialData prop with array of headings data. initialData is replaced with actual data on mount.

Use minDepthToOffset prop to set minimum depth at which offset should be applied. By default, minDepthToOffset is 1, which means that first and second level headings will not be offset. Set it to 0 to apply offset to all headings.

To control offset value in px, set depthOffset prop:

TableOfContents supports autoContrast prop and theme.autoContrast. If autoContrast is set either on TableOfContents or on theme, content color will be adjusted to have sufficient contrast with the value specified in color prop.

Note that autoContrast feature works only if you use color prop to change background color. autoContrast works only with filled variant.

Example of customizing TableOfContents with Styles API and data-* attributes:

By default, TableOfContents does not track changes in the DOM. If you want to update headings data after the parent component has mounted, you can use reinitializeRef to get reinitialize function from use-scroll-spy hook:

Build fully functional accessible web applications faster than ever

Bui

*[Content truncated - see full docs]*

**Examples**:

```python
import { TableOfContents } from '@mantine/core';

function Demo() {
  return (
    <TableOfContents
      variant="filled"
      color="blue"
      size="sm"
      radius="sm"
      scrollSpyOptions={{
        selector: '#mdx :is(h1, h2, h3, h4, h5, h6)',
      }}
      getControlProps={({ data }) => ({
        onClick: () => data.getNode().scrollIntoView(),
        children: data.value,
      })}
    />
  );
}
```

```python
import { TableOfContents } from '@mantine/core';

function Demo() {
  return (
    <TableOfContents
      scrollSpyOptions={{
        selector: '#mdx [data-heading]',
        getDepth: (element) => Number(element.getAttribute('data-order')),
        getValue: (element) => element.getAttribute('data-heading') || '',
      }}
    />
  );
}
```

```python
import { TableOfContents } from '@mantine/core';

function Demo() {
  return (
    <TableOfContents
      getControlProps={({ active, data }) => ({
        component: 'a',
        href: `#${data.id}`,
        style: { color: active ? 'blue' : 'gray' },
        children: data.value,
      })}
    />
  );
}
```

---

## Table | Mantine

**URL**: https://mantine.dev/core/table/

**Contents**:
- Table
- Usage
- data prop
- Sticky header
- Spacing
- Caption and tfoot
- Striped and rows hover
- Scroll container

Render table with theme styles

Table data for all examples:

You can use data prop to automatically generate table rows from array of React nodes. data prop accepts an object with the following properties:

Set stickyHeader to make table header sticky. To customize top position of the header use stickyHeaderOffset prop: it is useful when you have a fixed header in your application. For example, Mantine documentation website has a fixed header with 60px height:

To control spacing use horizontalSpacing and verticalSpacing props. Both props support spacing from theme.spacing and any valid CSS value to set cell padding:

Table support tfoot and caption elements. Set captionSide prop (top or bottom) to change caption position.

To prevent viewport overflow wrap Table with Table.ScrollContainer. The component accepts minWidth prop which sets minimum width below which table will be scrollable.

By default, Table.ScrollContainer uses ScrollArea, you can change it to native scrollbars by setting type="native":

You can also set maxHeight prop on Table.ScrollContainer to limit table height:

Set variant="vertical" to render table with vertical layout:

Set tabularNums prop to render numbers in tabular style. It sets font-variant-numeric: tabular-nums which makes numbers to have equal width. This is useful when you have columns with numbers and you want them to be aligned:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```javascript
const elements = [
  { position: 6, mass: 12.011, symbol: 'C', name: 'Carbon' },
  { position: 7, mass: 14.007, symbol: 'N', name: 'Nitrogen' },
  { position: 39, mass: 88.906, symbol: 'Y', name: 'Yttrium' },
  { position: 56, mass: 137.33, symbol: 'Ba', name: 'Barium' },
  { position: 58, mass: 140.12, symbol: 'Ce', name: 'Cerium' },
];
```

```python
import { Table } from '@mantine/core';

function Demo() {
  const rows = elements.map((element) => (
    <Table.Tr key={element.name}>
      <Table.Td>{element.position}</Table.Td>
      <Table.Td>{element.name}</Table.Td>
      <Table.Td>{element.symbol}</Table.Td>
      <Table.Td>{element.mass}</Table.Td>
    </Table.Tr>
  ));

  return (
    <Table>
      <Table.Thead>
        <Table.Tr>
          <Table.Th>Element position</Table.Th>
          <Table.Th>Element name</Table.Th>
          <Tab
...
```

```python
import { Table, TableData } from '@mantine/core';

const tableData: TableData = {
  caption: 'Some elements from periodic table',
  head: ['Element position', 'Atomic mass', 'Symbol', 'Element name'],
  body: [
    [6, 12.011, 'C', 'Carbon'],
    [7, 14.007, 'N', 'Nitrogen'],
    [39, 88.906, 'Y', 'Yttrium'],
    [56, 137.33, 'Ba', 'Barium'],
    [58, 140.12, 'Ce', 'Cerium'],
  ],
};

function Demo() {
  return <Table data={tableData} />;
}
```

---

## Tabs | Mantine

**URL**: https://mantine.dev/core/tabs/

**Contents**:
- Tabs
- Usage
- Controlled Tabs
- Uncontrolled Tabs
- Change colors
- Tabs position
- Inverted tabs
- Vertical tabs placement

Switch between different views

To control Tabs state, use value and onChange props:

If you do not need to subscribe to Tabs state changes, use defaultValue:

To change colors of all tabs, set color on Tabs component, to change color of the individual tab, set color on Tabs.Tab.

To display tab on the opposite side, set margin-left: auto with ml="auto" prop or with className:

To make tabs inverted, place Tabs.Panel components before Tabs.List and add inverted prop to Tabs component:

To change placement of Tabs.List in vertical orientation set placement prop:

Example of custom variant with FloatingIndicator:

Set disabled prop on Tabs.Tab component to disable tab. Disabled tab cannot be activated with mouse or keyboard, and they will be skipped when user navigates with arrow keys:

By default, tabs are activated when user presses arrows keys or Home/End keys. To disable that set activateTabWithKeyboard={false} on Tabs component:

By default, active tab cannot be deactivated. To allow that set allowTabDeactivation on Tabs component:

By default, inactive Tabs.Panel will stay mounted, to unmount inactive tabs, set keepMounted={false} on Tabs. This is useful when you want to render components that impact performance inside Tabs.Panel. Note that components that are rendered inside Tabs.Panel will reset their state on each mount (tab change).

Tabs supports Styles API, you can add styles to any inner element of the component withclassNames prop. Follow Styles API documentation to learn more.

Hover over selectors to highlight corresponding elements

Root element (`Tabs` component)

List of tabs (`Tabs.List` component)

Panel with tab content (`Tabs.Panel` component)

Tab button (`Tabs.Tab` component)

Left and right sections of `Tabs.Tab`

Example of Styles API usage to customize tab styles:

Tabs component follows WAI-ARIA recommendations on accessibility.

If you use Tabs.Tab without text content, for example, only with icon, then set aria-label or use VisuallyHidde

*[Content truncated - see full docs]*

**Examples**:

```python
import { Tabs } from '@mantine/core';
import { IconPhoto, IconMessageCircle, IconSettings } from '@tabler/icons-react';

function Demo() {
  return (
    <Tabs defaultValue="gallery">
      <Tabs.List>
        <Tabs.Tab value="gallery" leftSection={<IconPhoto size={12} />}>
          Gallery
        </Tabs.Tab>
        <Tabs.Tab value="messages" leftSection={<IconMessageCircle size={12} />}>
          Messages
        </Tabs.Tab>
        <Tabs.Tab value="settings" leftSection={<IconSettings size
...
```

```python
import { useState } from 'react';
import { Tabs } from '@mantine/core';

function Demo() {
  const [activeTab, setActiveTab] = useState<string | null>('first');

  return (
    <Tabs value={activeTab} onChange={setActiveTab}>
      <Tabs.List>
        <Tabs.Tab value="first">First tab</Tabs.Tab>
        <Tabs.Tab value="second">Second tab</Tabs.Tab>
      </Tabs.List>

      <Tabs.Panel value="first">First panel</Tabs.Panel>
      <Tabs.Panel value="second">Second panel</Tabs.Panel>
    </Tabs>

...
```

```python
import { Tabs } from '@mantine/core';

function Demo() {
  return (
    <Tabs defaultValue="first">
      <Tabs.List>
        <Tabs.Tab value="first">First tab</Tabs.Tab>
        <Tabs.Tab value="second">Second tab</Tabs.Tab>
      </Tabs.List>

      <Tabs.Panel value="first">First panel</Tabs.Panel>
      <Tabs.Panel value="second">Second panel</Tabs.Panel>
    </Tabs>
  );
}
```

---

## TagsInput | Mantine

**URL**: https://mantine.dev/core/tags-input/

**Contents**:
- TagsInput
- Made with Combobox
- Usage
- Controlled
- Controlled search value
- Clearable
- Max selected values
- Accept value on blur

Capture a list of values from user with free input and suggestions

TagsInput is an opinionated component built on top of Combobox component. It has a limited set of features to cover only the basic use cases. If you need more advanced features, you can build your own component with Combobox. You can find examples of custom tags input components on the examples page.

TagsInput provides a way to enter multiple values. It can be used with suggestions or without them. TagsInput is similar to MultiSelect, but it allows entering custom values.

TagsInput value must be an array of strings, other types are not supported. onChange function is called with an array of strings as a single argument.

You can control search value with searchValue and onSearchChange props:

Set clearable prop to display the clear button in the right section. The button is not displayed when:

You can limit the number of selected values with maxTags prop. This will not allow adding more values once the limit is reached.

By default, if the user types a value and blurs the input, the value is added to the list. You can change this behavior by setting acceptValueOnBlur to false. In this case, the value is added only when the user presses Enter or clicks on a suggestion.

By default, TagsInput does not allow to add duplicate values, but you can change this behavior by setting allowDuplicates prop. Value is considered duplicate if it is already present in the value array, regardless of the case and trailing whitespace.

You can use isDuplicate prop to control how duplicates are detected. It is a function that receives two arguments: tag value and current tags. The function must return true if the value is duplicate.

Example of using isDuplicate to allow using the same value with different casing:

By default, TagsInput splits values by comma (,), you can change this behavior by setting splitChars prop to an array of strings. All values from splitChars cannot be included in the final value. Values ar

*[Content truncated - see full docs]*

**Examples**:

```python
import { TagsInput } from '@mantine/core';

function Demo() {
  return <TagsInput label="Press Enter to submit a tag" placeholder="Enter tag" />;
}
```

```python
import { useState } from 'react';
import { TagsInput } from '@mantine/core';

function Demo() {
  const [value, setValue] = useState<string[]>([]);
  return <TagsInput data={[]} value={value} onChange={setValue} />;
}
```

```python
import { useState } from 'react';
import { TagsInput } from '@mantine/core';

function Demo() {
  const [searchValue, setSearchValue] = useState('');
  return (
    <TagsInput
      searchValue={searchValue}
      onSearchChange={setSearchValue}
      data={[]}
    />
  );
}
```

---

## TextInput | Mantine

**URL**: https://mantine.dev/core/text-input/

**Contents**:
- TextInput
- Usage
- Controlled
- Left and right sections
- Error state
- Disabled state
- Styles API
- Get element ref

Capture string input from user

TextInput component supports Input and Input.Wrapper components features and all input element props. TextInput documentation does not include all features supported by the component – see Input documentation to learn about all available features.

TextInput supports leftSection and rightSection props. These sections are rendered with absolute position inside the input wrapper. You can use them to display icons, input controls or any other elements.

You can use the following props to control sections styles and content:

TextInput supports Styles API, you can add styles to any inner element of the component withclassNames prop. Follow Styles API documentation to learn more.

Hover over selectors to highlight corresponding elements

Root element of the Input

Left and right sections

Required asterisk element, rendered inside label

If TextInput is used without label prop, it will not be announced properly by screen reader:

Set aria-label to make the input accessible. In this case label will not be visible, but screen reader will announce it:

If label prop is set, input will be accessible it is not required to set aria-label:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { TextInput } from '@mantine/core';

function Demo() {
  return (
    <TextInput
      label="Input label"
      description="Input description"
      placeholder="Input placeholder"
    />
  );
}
```

```python
import { useState } from 'react';
import { TextInput } from '@mantine/core';

function Demo() {
  const [value, setValue] = useState('');
  return (
    <TextInput
      value={value}
      onChange={(event) => setValue(event.currentTarget.value)}
    />
  );
}
```

```python
import { TextInput } from '@mantine/core';
import { IconAt } from '@tabler/icons-react';

function Demo() {
  const icon = <IconAt size={16} />;
  return (
    <>
      <TextInput
        leftSectionPointerEvents="none"
        leftSection={icon}
        label="Your email"
        placeholder="Your email"
      />
      <TextInput
        mt="md"
        rightSectionPointerEvents="none"
        rightSection={icon}
        label="Your email"
        placeholder="Your email"
      />
    </>
  );

...
```

---

## Text | Mantine

**URL**: https://mantine.dev/core/text/

**Contents**:
- Text
- Usage
- Gradient variant
- Truncate
- Line clamp
  - Line clamp with Typography
- Inherit styles
  - Title in which you want to highlight something

When variant prop is set to gradient, you can control gradient with gradient prop, it accepts an object with from, to and deg properties. If thegradient prop is not set, Text will use theme.defaultGradient which can be configured on the theme object. gradient prop is ignored when variant is not gradient.

Note that variant="gradient" supports only linear gradients with two colors. If you need a more complex gradient, then use Styles API to modify Text styles.

Set truncate prop to add text-overflow: ellipsis styles:

Lorem ipsum dolor sit amet consectetur adipisicing elit. Unde provident eos fugiat id necessitatibus magni ducimus molestias. Placeat, consequatur. Quisquam, quae magnam perspiciatis excepturi iste sint itaque sunt laborum. Nihil?

Specify maximum number of lines with lineClamp prop. This option uses -webkit-line-clamp CSS property (caniuse). Note that padding-bottom cannot be set on text element:

From Bulbapedia: Bulbasaur is a small, quadrupedal Pokémon that has blue-green skin with darker patches. It has red eyes with white pupils, pointed, ear-like structures on top of its head, and a short, blunt snout with a wide mouth. A pair of small, pointed teeth are visible in the upper jaw when its mouth is open. Each of its thick legs ends with three sharp claws. On Bulbasaur's back is a green plant bulb, which is grown from a seed planted there at birth. The bulb also conceals two slender, tentacle-like vines and provides it with energy through photosynthesis as well as from the nutrient-rich seeds contained within.

Line clamp can also be used with any children (not only strings), for example with Typography:

Lorem ipsum dolor sit amet consectetur adipisicing elit. Nesciunt nulla quam aut sed corporis voluptates praesentium inventore, sapiente ex tempore sit consequatur debitis non! Illo cum ipsa reiciendis quidem facere, deserunt eos totam impedit. Vel ab, ipsum veniam aperiam odit molestiae incidunt minus, sint eos iusto earum quaerat vitae perspiciat

*[Content truncated - see full docs]*

**Examples**:

```python
import { Text } from '@mantine/core';

function Demo() {
  return (
    <>
      <Text size="xs">Extra small text</Text>
      <Text size="sm">Small text</Text>
      <Text size="md">Default text</Text>
      <Text size="lg">Large text</Text>
      <Text size="xl">Extra large text</Text>
      <Text fw={500}>Semibold</Text>
      <Text fw={700}>Bold</Text>
      <Text fs="italic">Italic</Text>
      <Text td="underline">Underlined</Text>
      <Text td="line-through">Strikethrough</Text>
      <
...
```

```python
import { Text } from '@mantine/core';

function Demo() {
  return (
    <Text
      size="xl"
      fw={900}
      variant="gradient"
      gradient={{ from: 'blue', to: 'cyan', deg: 90 }}
    >
      Gradient Text
    </Text>
  );
}
```

```python
import { Text, Box } from '@mantine/core';

function Demo() {
  return (
    <Box w={300}>
      <Text truncate="end">
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Unde provident eos fugiat id
        necessitatibus magni ducimus molestias. Placeat, consequatur. Quisquam, quae magnam
        perspiciatis excepturi iste sint itaque sunt laborum. Nihil?
      </Text>
    </Box>
  );
}
```

---

## Textarea | Mantine

**URL**: https://mantine.dev/core/textarea/

**Contents**:
- Textarea
- Usage
- Controlled
- Autosize
- Enable resize
- Error state
- Disabled state
- Styles API

Autosize or regular textarea

Textarea component supports Input and Input.Wrapper components features and all textarea element props. Textarea documentation does not include all features supported by the component – see Input documentation to learn about all available features.

Autosize textarea uses react-textarea-autosize package. Textarea height will grow until maxRows are reached or indefinitely if maxRows not set.

By default, resize is none, to enable it set resize prop to vertical or both:

Textarea supports Styles API, you can add styles to any inner element of the component withclassNames prop. Follow Styles API documentation to learn more.

Hover over selectors to highlight corresponding elements

Root element of the Input

Left and right sections

Required asterisk element, rendered inside label

If Textarea is used without label prop, it will not be announced properly by screen reader:

Set aria-label to make the input accessible. In this case label will not be visible, but screen reader will announce it:

If label prop is set, input will be accessible it is not required to set aria-label:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { Textarea } from '@mantine/core';

function Demo() {
  return (
    <Textarea
      label="Input label"
      description="Input description"
      placeholder="Input placeholder"
    />
  );
}
```

```python
import { useState } from 'react';
import { Textarea } from '@mantine/core';

function Demo() {
  const [value, setValue] = useState('');
  return (
    <Textarea
      value={value}
      onChange={(event) => setValue(event.currentTarget.value)}
    />
  );
}
```

```python
import { Textarea } from '@mantine/core';

function Demo() {
  return (
    <>
      <Textarea
        placeholder="Autosize with no rows limit"
        label="Autosize with no rows limit"
        autosize
        minRows={2}
      />

      <Textarea
        label="Autosize with 4 rows max"
        placeholder="Autosize with 4 rows max"
        autosize
        minRows={2}
        maxRows={4}
      />
    </>
  );
}
```

---

## ThemeIcon | Mantine

**URL**: https://mantine.dev/core/theme-icon/

**Contents**:
- ThemeIcon
- Usage
- Gradient variant
- Customize variants colors
- autoContrast

Render icon inside element with theme colors

When variant prop is set to gradient, you can control gradient with gradient prop, it accepts an object with from, to and deg properties. If thegradient prop is not set, ThemeIcon will use theme.defaultGradient which can be configured on the theme object. gradient prop is ignored when variant is not gradient.

Note that variant="gradient" supports only linear gradients with two colors. If you need a more complex gradient, then use Styles API to modify ThemeIcon styles.

You can customize colors for ThemeIcon and other components variants by adding variantColorResolver to your theme.

ThemeIcon supports autoContrast prop and theme.autoContrast. If autoContrast is set either on ThemeIcon or on theme, content color will be adjusted to have sufficient contrast with the value specified in color prop.

Note that autoContrast feature works only if you use color prop to change background color. autoContrast works only with filled variant.

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { ThemeIcon } from '@mantine/core';
import { IconPhoto } from '@tabler/icons-react';

function Demo() {
  return (
    <ThemeIcon>
      <IconPhoto style={{ width: '70%', height: '70%' }} />
    </ThemeIcon>
  );
}
```

```python
import { ThemeIcon } from '@mantine/core';
import { IconHeart } from '@tabler/icons-react';

function Demo() {
  return (
    <ThemeIcon
      variant="gradient"
      size="xl"
      aria-label="Gradient action icon"
      gradient={{ from: 'blue', to: 'cyan', deg: 90 }}
    >
      <IconHeart />
    </ThemeIcon>
  );
}
```

```python
import { IconPhoto, IconFingerprint, IconError404 } from '@tabler/icons-react';
import {
  ThemeIcon,
  Group,
  MantineProvider,
  defaultVariantColorsResolver,
  VariantColorsResolver,
  parseThemeColor,
  rgba,
  darken,
} from '@mantine/core';

const variantColorResolver: VariantColorsResolver = (input) => {
  const defaultResolvedColors = defaultVariantColorsResolver(input);
  const parsedColor = parseThemeColor({
    color: input.color || input.theme.primaryColor,
    theme: input.theme,
 
...
```

---

## Timeline | Mantine

**URL**: https://mantine.dev/core/timeline/

**Contents**:
- Timeline
- Usage
- Line and bullet props
- Bullet as React node
- Wrap Timeline.Item

Display list of events in chronological order

You've created new branch fix-notifications from master

You've pushed 23 commits to fix-notifications branch

You've submitted a pull request Fix incorrect notification message (#187)

Robert Gluesticker left a code review on your pull request

Control timeline appearance with the following props:

You've created new branch fix-notifications from master

You've pushed 23 commits to fix-notifications branch

You've submitted a pull request Fix incorrect notification message (#187)

Robert Gluesticker left a code review on your pull request

Default bullet without anything

Timeline bullet as avatar image

Timeline bullet as icon

Timeline bullet as ThemeIcon component

Timeline component relies on Timeline.Item order. Wrapping Timeline.Item is not supported, Instead you will need to use different approaches:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { Timeline, Text } from '@mantine/core';
import { IconGitBranch, IconGitPullRequest, IconGitCommit, IconMessageDots } from '@tabler/icons-react';

function Demo() {
  return (
    <Timeline active={1} bulletSize={24} lineWidth={2}>
      <Timeline.Item bullet={<IconGitBranch size={12} />} title="New branch">
        <Text c="dimmed" size="sm">You&apos;ve created new branch <Text variant="link" component="span" inherit>fix-notifications</Text> from master</Text>
        <Text size="xs" mt=
...
```

```python
import { Timeline } from '@mantine/core';

function Demo() {
  return (
    <Timeline active={1} bulletSize={25}>
      {/* items */}
    </Timeline>
  );
}
```

```python
import { ThemeIcon, Text, Avatar, Timeline } from '@mantine/core';
import { IconSun, IconVideo } from '@tabler/icons-react';

function Demo() {
  return (
    <Timeline bulletSize={24}>
      <Timeline.Item title="Default bullet">
        <Text c="dimmed" size="sm">
          Default bullet without anything
        </Text>
      </Timeline.Item>
      <Timeline.Item
        title="Avatar"
        bullet={
          <Avatar
            size={22}
            radius="xl"
            src="https://av
...
```

---

## Title | Mantine

**URL**: https://mantine.dev/core/title/

**Contents**:
- Title
- Usage
- This is h1 title
- This is h2 title
  - This is h3 title
    - This is h4 title
      - This is h5 title
        - This is h6 title

Use Title component to render h1-h6 headings with Mantine theme styles. By default, Title has no margins and paddings. You can change font-size, font-weight and line-height per heading with theme.headings.

Set order prop to render a specific element (h1-h6), default order is 1:

You can change Title size independent of its order:

Use textWrap prop to control text-wrap CSS property. It controls how text inside an element is wrapped.

You can also set textWrap on theme:

Set lineClamp prop to truncate text after specified number of lines:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { Title } from '@mantine/core';

function Demo() {
  return (
    <>
      <Title order={1}>This is h1 title</Title>
      <Title order={2}>This is h2 title</Title>
      <Title order={3}>This is h3 title</Title>
      <Title order={4}>This is h4 title</Title>
      <Title order={5}>This is h5 title</Title>
      <Title order={6}>This is h6 title</Title>
    </>
  );
}
```

```python
import { Title } from '@mantine/core';

function Demo() {
  return (
    <>
      <Title order={3} size="h1">
        H3 heading with h1 font-size
      </Title>
      <Title size="h4">H1 heading with h4 font-size</Title>
      <Title size={16}>H1 heading with 16px size</Title>
      <Title size="xs">H1 heading with xs size</Title>
    </>
  );
}
```

```python
import { Title } from '@mantine/core';

function Demo() {
  return (
    <Title order={3} textWrap="wrap">
      Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quasi voluptatibus inventore iusto
      cum dolore molestiae perspiciatis! Totam repudiandae impedit maxime!
    </Title>
  );
}
```

---

## Tooltip | Mantine

**URL**: https://mantine.dev/core/tooltip/

**Contents**:
- Tooltip
- Usage
- Tooltip children
- Tooltip target
- Required ref prop
- Color
- Offset
- Arrow

Renders tooltip at given element on mouse over or other event

Tooltip requires an element or a component as a single child – strings, fragments, numbers and multiple elements/components are not supported and will throw error. Custom components must provide a prop to get root element ref, all Mantine components support ref out of the box.

target prop is an alternative to children. It accepts a string (selector), an HTML element or a ref object with HTML element. Use target prop when you do not render tooltip target as JSX element.

Example of using target prop with a string selector:

Custom components that are rendered inside Tooltip are required to support ref prop:

Use forwardRef function to forward ref to root element:

Set offset prop to a number to change tooltip position relative to the target element. This way you can control tooltip offset on main axis only.

To control offset on both axis, pass object with mainAxis and crossAxis properties:

Set withArrow prop to add an arrow to the tooltip. Arrow is a div element rotated with transform: rotate(45deg).

arrowPosition prop determines how arrow is position relative to the target element when position is set to *-start and *-end values on Popover component. By default, the value is center – the arrow is positioned in the center of the target element if it is possible.

If you change arrowPosition to side, then the arrow will be positioned on the side of the target element, and you will be able to control arrow offset with arrowOffset prop. Note that when arrowPosition is set to center, arrowOffset prop is ignored.

Events that trigger tooltip can be changed with events prop, it accepts an object with the following properties that determine which events will trigger tooltip:

To enable multiline mode, set multiline prop to enable line breaks and w style prop to set tooltip width:

Set inline prop to use Tooltip with inline elements:

Stantler’s magnificent antlers were traded at high prices as works of art. 

*[Content truncated - see full docs]*

**Examples**:

```python
import { Tooltip, Button } from '@mantine/core';

function Demo() {
  return (
    <Tooltip label="Tooltip">
      <Button>Button with tooltip</Button>
    </Tooltip>
  );
}
```

```python
import { Badge, Tooltip } from '@mantine/core';

function Demo() {
  return (
    <>
      <Tooltip label="OK">
        <button>Native button – ok</button>
      </Tooltip>

      <Tooltip label="OK">
        <Badge>Mantine component – ok</Badge>
      </Tooltip>

      <Tooltip label="Throws">
        Raw string, NOT OK – will throw error
      </Tooltip>

      {/* Number, NOT OK – will throw error */}
      <Tooltip label="Throws">{2}</Tooltip>

      <Tooltip label="Throws">
        <>Fragme
...
```

```python
import { Button, Tooltip } from '@mantine/core';

function Demo() {
  return (
    <>
      <Tooltip target="#hover-me" label="Tooltip over button" />
      <Button id="hover-me">Hover me to see tooltip</Button>
    </>
  );
}
```

---

## Transition | Mantine

**URL**: https://mantine.dev/core/transition/

**Contents**:
- Transition
- Premade transitions
- Custom transitions
- Enter and exit delay

Animate presence of component with pre-made animations

Mantine includes several premade transitions:

To use one of them set transition property to one of these values:

You can create your own transition. transition is an object with 4 properties:

Use enterDelay and exitDelay props to delay transition start. Values are in milliseconds:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { Transition } from '@mantine/core';

function Demo({ opened }: { opened: boolean }) {
  return (
    <Transition
      mounted={opened}
      transition="fade"
      duration={400}
      timingFunction="ease"
    >
      {(styles) => <div style={styles}>Your modal</div>}
    </Transition>
  );
}
```

```python
import { useState } from 'react';
import { useClickOutside } from '@mantine/hooks';
import { Transition, Paper, Button, Box } from '@mantine/core';

const scaleY = {
  in: { opacity: 1, transform: 'scaleY(1)' },
  out: { opacity: 0, transform: 'scaleY(0)' },
  common: { transformOrigin: 'top' },
  transitionProperty: 'transform, opacity',
};

function Demo() {
  const [opened, setOpened] = useState(false);
  const clickOutsideRef = useClickOutside(() => setOpened(false));

  return (
    <Box
  
...
```

```python
import { useState } from 'react';
import { Button, Flex, Paper, Transition } from '@mantine/core';

export function Demo() {
  const [opened, setOpened] = useState(false);

  return (
    <Flex maw={200} pos="relative" justify="center" m="auto">
      <Button onClick={() => setOpened(true)}>Open dropdown</Button>

      <Transition mounted={opened} transition="pop" enterDelay={500} exitDelay={300}>
        {(transitionStyle) => (
          <Paper
            shadow="md"
            p="xl"
      
...
```

---

## Tree | Mantine

**URL**: https://mantine.dev/core/tree/

**Contents**:
- Tree
- Usage
- Data prop
- Data type
- renderNode
- useTree hook
- Checked state
- Initial expanded state

Display a Tree structure

Tree component is used to display hierarchical data. Tree component has minimal styling by default, you can customize styles with Styles API.

Data passed to the data prop should follow these rules:

Invalid data example:

You can import TreeNodeData type to define data type for your tree:

Use renderNode prop to customize node rendering. renderNode function receives an object with the following properties as a single argument:

useTree hook can be used to control selected and expanded state of the tree.

The hook accepts an object with the following properties:

And returns an object with the following properties:

You can pass the value returned by the useTree hook to the tree prop of the Tree component to control tree state:

Tree can be used to display checked state with checkboxes. To implement checked state, you need to render Checkbox.Indicator in the renderNode function:

To check/uncheck nodes, use checkAllNodes and uncheckAllNodes functions:

Expanded state is an object of node.value and boolean values that represent nodes expanded state. To change initial expanded state, pass initialExpandedState to the useTree hook. To generate expanded state from data with expanded nodes, you can use getTreeExpandedState function: it accepts data and an array of expanded nodes values and returns expanded state object.

If '*' is passed as the second argument to getTreeExpandedState, all nodes will be expanded:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { Tree } from '@mantine/core';
import { data } from './data';

function Demo() {
  return <Tree data={data} />;
}
```

```javascript
// ✅ Valid data, all values are unique
const data = [
  {
    value: 'src',
    label: 'src',
    children: [
      { value: 'src/components', label: 'components' },
      { value: 'src/hooks', label: 'hooks' },
    ],
  },
  { value: 'package.json', label: 'package.json' },
];
```

```javascript
// ❌ Invalid data, values are not unique (components is used twice)
const data = [
  {
    value: 'src',
    label: 'src',
    children: [{ value: 'components', label: 'components' }],
  },
  { value: 'components', label: 'components' },
];
```

---

## Typography | Mantine

**URL**: https://mantine.dev/core/typography/

**Contents**:
- Typography
- Usage
- Example
- Example article
- Article itself
  - Your team is “we”
  - The wider organization
- All styles demo

Styles provider for html content

Mantine does not include typography global styles. Use Typography to add typography styles to your html content:

This is example article from CSS-Tricks website written by Sarah Drasner. It is used as an example to showcase real world styles of Typography component, please read full article on CSS-Tricks website.

Let’s talk for a moment about how we talk about our teams. This might not seem like something that needs a whole article dedicated to it, but it’s actually quite crucial. The way that we refer to our teams sends signals: to stakeholders, to your peers, to the team itself, and even to ourselves. In addressing how we speak about our teams, we’ll also talk about accountability.

I have noticed shared similarities in those folks I consider good managers whose teams deliver well, and those who don’t. It starts with how they communicate about their teams.

There can be a perception that as a manager of an organization you are in control at all times. Part of that control can invariably be perceived as how you appear to be in charge, are competent, or how you personally perform. Due to that, some bad behaviors can arise- not due to malice, but due to fear. For this reason, it can be tempting to take credit for success and avoid credit when there is failure.

The irony is that the more that you try to hold on to these external perceptions, the more it will slip away. Why? Because the problems you are solving as a manager really aren’t about you.

Your team is “we”. You are a driving force of that team, no matter how high up the hierarchy chain. What happens on that team is your responsibility. When you speak about your org, you should include yourself in the statement.

When your team succeeds in something though, then you can praise them and leave yourself out of it. Here’s an example:

They really pulled this project over the line, despite the incredibly tight project timeline. Everyone showed up and was driven throughout the e

*[Content truncated - see full docs]*

**Examples**:

```python
import { Typography } from '@mantine/core';

function Demo() {
  return (
    <Typography>
      <div
        dangerouslySetInnerHTML={{ __html: '<p>Your html here</p>' }}
      />
    </Typography>
  );
}
```

```python
import { Typography } from '@mantine/core';

const html = '...html content here...';

function Demo() {
  return (
    <Typography>
      <div dangerouslySetInnerHTML={{ __html: html }} />
    </Typography>
  );
}
```

---

## UnstyledButton | Mantine

**URL**: https://mantine.dev/core/unstyled-button/

**Contents**:
- UnstyledButton
- Usage
- Polymorphic component
- Get element ref

Unstyled polymorphic button

UnstyledButton resets default button styles, it is used as a base for all other button components. You can use it to as a base for custom polymorphic buttons.

UnstyledButton is a polymorphic component – its default root element is button, but it can be changed to any other element or component with component prop:

Polymorphic components with TypeScript

Note that polymorphic components props types are different from regular components – they do not extend HTML element props of the default element. For example, UnstyledButtonProps does not extend React.ComponentPropsWithoutRef'<'div'>' although button is the default element.

If you want to create a wrapper for a polymorphic component that is not polymorphic (does not support component prop), then your component props interface should extend HTML element props, for example:

If you want your component to remain polymorphic after wrapping, use createPolymorphicComponent function described in this guide.

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { UnstyledButton } from '@mantine/core';

function Demo() {
  return <UnstyledButton>Button without styles</UnstyledButton>;
}
```

```python
import { UnstyledButton } from '@mantine/core';

function Demo() {
  return <UnstyledButton component="a" />;
}
```

```python
import type { UnstyledButtonProps, ElementProps } from '@mantine/core';

interface MyUnstyledButtonProps extends UnstyledButtonProps,
  ElementProps<'a', keyof UnstyledButtonProps> {}
```

---

## Usage with React Router | Mantine

**URL**: https://mantine.dev/guides/react-router/

**Contents**:
- Usage with React Router
- Generate new application
- Installation
- PostCSS setup
- Setup

Follow React Router getting started guide guide to create new React Router application:

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

Add styles imports, MantineProvider and ColorSchemeScript to app/root.tsx:

All set! Start development server:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```text
npx create-react-router@latest my-react-router-app
```

```text
yarn add @mantine/core @mantine/hooks
```

```text
npm install @mantine/core @mantine/hooks
```

---

## Usage with TypeScript | Mantine

**URL**: https://mantine.dev/guides/typescript/

**Contents**:
- Usage with TypeScript
- Components props types
- ElementProps type
- MantineTheme type
- MantineThemeOverride type
- MantineColorScheme type
- MantineSize type
- Theme object declarations

All @mantine/* packages are fully compatible with TypeScript. All examples in the documentation are written in TypeScript – you can copy-paste them to your project without any changes.

This guide will help you get familiar with types that @mantine/core package exports.

Each @mantine/ package that exports components, exports props types for these components as well. You can import component props types by adding Props to the component name, for example, you can import Button and DatePicker components props like so:

Note that there are two variations of props types: for polymorphic components and for regular components. Regular components props types include React.ComponentPropsWithoutRef<'X'>, where X is the root element type, for example 'div'.

Example of extending regular component props:

Polymorphic components props types do not include React.ComponentPropsWithoutRef<'X'> because their root element depends on the component prop value.

Example of extending polymorphic components props:

ElementProps is a utility type similar to React.ComponentPropsWithoutRef, but with additional features. It replaces native elements style prop with Mantine style prop and allows omitting properties that are passed as a second type.

MantineTheme is a type of theme object. You can use it to add types to functions that accept theme object as an argument:

MantineThemeOverride type is a deep partial of MantineTheme. It can be used in functions that accept theme override as an argument:

MantineColorScheme is a union of 'light' | 'dark' | 'auto' values. You can use to add types to function that accept color scheme as an argument:

MantineSize type is a union of 'xs' | 'sm' | 'md' | 'lg' | 'xl' values. You can use to add types to various props that accept size as an argument, for example, radius, shadow, p.

You can change theme.other and theme.colors types by extending MantineTheme interface in .d.ts file. Create mantine.d.ts anywhere in your project (must be included in tsconfig.

*[Content truncated - see full docs]*

**Examples**:

```python
import type { ButtonProps } from '@mantine/core';
import type { DatePickerProps } from '@mantine/dates';
```

```python
import { Group, GroupProps } from '@mantine/core';

// Interface includes `React.ComponentPropsWithoutRef<'div'>`
interface MyGroupProps extends GroupProps {
  spacing: number;
}

function MyGroup({ spacing, ...others }: MyGroupProps) {
  return <Group my={spacing} {...others} />;
}
```

```python
import { Button, ButtonProps, ElementProps } from '@mantine/core';

interface MyButtonProps
  extends ButtonProps,
    ElementProps<'button', keyof ButtonProps> {
  height: number;
}

function MyButton({ height, ...others }: MyButtonProps) {
  return <Button style={{ height }} {...others} />;
}
```

---

## VisuallyHidden | Mantine

**URL**: https://mantine.dev/core/visually-hidden/

**Contents**:
- VisuallyHidden
- Usage

Hide element visually but keep it accessible for screen readers

VisuallyHidden is a utility component that hides content visually but leaves it available to screen readers.

For example, it can be used with ActionIcon component:

Build fully functional accessible web applications faster than ever

Built by Vitaly Rtishchev and these awesome people

**Examples**:

```python
import { IconHeart } from '@tabler/icons-react';
import { ActionIcon, VisuallyHidden } from '@mantine/core';

function Demo() {
  return (
    <ActionIcon>
      <IconHeart />
      <VisuallyHidden>Like post</VisuallyHidden>
    </ActionIcon>
  );
}
```

---
