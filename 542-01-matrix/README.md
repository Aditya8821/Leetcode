<h2><a href="https://leetcode.com/problems/01-matrix/">542. 01 Matrix</a></h2><h3>Medium</h3><hr><div class=""><p class="">Given an <code class="">m x n</code> binary matrix <code class="">mat</code>, return <em class="">the distance of the nearest </em><code class="">0</code><em class=""> for each cell</em>.</p>

<p class="">The distance between two adjacent cells is <code class="">1</code>.</p>

<p class="">&nbsp;</p>
<p class=""><strong class="">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/24/01-1-grid.jpg" style="width: 253px; height: 253px;">
<pre class=""><strong class="">Input:</strong> mat = [[0,0,0],[0,1,0],[0,0,0]]
<strong class="">Output:</strong> [[0,0,0],[0,1,0],[0,0,0]]
</pre>

<p class=""><strong class="">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/24/01-2-grid.jpg" style="width: 253px; height: 253px;">
<pre class=""><strong class="">Input:</strong> mat = [[0,0,0],[0,1,0],[1,1,1]]
<strong class="">Output:</strong> [[0,0,0],[0,1,0],[1,2,1]]
</pre>

<p class="">&nbsp;</p>
<p class=""><strong class="">Constraints:</strong></p>

<ul class="">
	<li class=""><code class="">m == mat.length</code></li>
	<li class=""><code class="">n == mat[i].length</code></li>
	<li class=""><code class="">1 &lt;= m, n &lt;= 10<sup class="">4</sup></code></li>
	<li class=""><code class="">1 &lt;= m * n &lt;= 10<sup class="">4</sup></code></li>
	<li class=""><code class="">mat[i][j]</code> is either <code class="">0</code> or <code class="">1</code>.</li>
	<li class="">There is at least one <code class="">0</code> in <code class="">mat</code>.</li>
</ul>
</div>