# OpenCV_converter
<h3>
	This GUI enables you to simply pick an image from your computer and by a click of a button, the image will be resized and edited, so that it can be applied for ComputerVision experiments.
</h3>

There are two options to choose from:
<ol>
	<li>The image is grayed out and the GaussianBlur() is applied.</li>
	<li>The image is grayed out and the threshold() function is applied. </li>
</ol>

Additionally, if the image is in portrait mode, a button "Rotate image" is made available to set the image straight, using <b><i>img.transpose(Image.ROTATE_270)</i></b>.  <strong>Image</strong> is the module, <b>transpose(method)</b> is the function.
