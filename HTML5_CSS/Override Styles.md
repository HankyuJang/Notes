# Override All Other Styles by using Important

CSS declarations < in-line styles < important

In CSS Declarations: element < class < id

If there're two classes for an element, second class override the first class.

```
<style>
  body {
    background-color: black;
    font-family: Monospace;
    color: green;
  }
  #orange-text {
    color: orange;
  }
  .pink-text {
    color: pink !important;
  }
  .blue-text {
    color: blue;
  }
</style>
<h1 id="orange-text" class="pink-text blue-text" style="color: white">Hello World!</h1>
```



Result: h1 element will have pink color
