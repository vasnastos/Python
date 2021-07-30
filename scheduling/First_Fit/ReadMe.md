<html>
<body>
<h1>First Fit Graph Coloring Algorithm</h1>
<hr>
<p><u>First Fit is the basic Greedy Algorithm to assign colors. It doesn’t guarantee to use minimum colors, but it guarantees an upper bound on the number of colors. The basic algorithm never uses more than d+1 colors where d is the maximum degree of a vertex in the given graph.</u></p>
<br>
<div>
1. Color first vertex with first color.<br>
2. Do following for remaining V-1 vertices.<br>
<ul>
   <li> Consider the currently picked vertex and color it with the
lowest numbered color that has not been used on any previously
colored vertices adjacent to it. If all previously used colors
appear on vertices adjacent to v, assign a new color to it.
</li>
</ul>
</div>
</body>
</html>