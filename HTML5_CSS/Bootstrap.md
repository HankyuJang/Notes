# Waypoint: Use Responsive Design with Bootstrap Fluid Containers

Now let's go back to our Cat Photo App. This time, we'll style it using the popular Bootstrap responsive CSS framework.

Bootstrap will figure out how wide your screen is and respond by resizing your HTML elements - hence the name `Responsive Design`.

With responsive design, there is no need to design a mobile version of your website. It will look good on devices with screens of any width.

You can add Bootstrap to any app just by including it by adding the following code to the top of your HTML:
```
<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css"/>
```
To get started, we should nest all of our HTML in a `div` element with the class `container-fluid`.

### Waypoint: Make Images Mobile Responsive

First, add a new image below the existing one. Set its `src` attribute to http://bit.ly/fcc-running-cats.

It would be great if this image could be exactly the width of our phone's screen.

Fortunately, with Bootstrap, all we need to do is add the `img-responsive` class to your image. Do this, and the image should perfectly fit the width of your page.

### Waypoint: Center Text with Bootstrap

Now that we're using Bootstrap, we can center our heading element to make it look better. All we need to do is add the class `text-center` to our `h2` element.

Remember that you can add several classes to the same element by separating each of them with a space, like this:
```
<h2 class="red-text text-center">your text</h2>
```

### Waypoint: Create a Bootstrap Button

Bootstrap has its own styles for `button` elements, which look much better than the plain HTML ones.

`<button class="btn">Like</button>`

### Waypoint: Create a Block Element Bootstrap Button

Normally, your `button` elements are only as wide as the text that they contain. By making them block elements, your button will stretch to fill your page's entire horizontal space and any elements following it will flow onto a "new line" below the block.

This image illustrates the difference between `inline` elements and `block-level` elements:

![button](http://i.imgur.com/O32cDWE.png)

Note that these buttons still need the `btn` class.
