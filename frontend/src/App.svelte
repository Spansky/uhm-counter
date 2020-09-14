<script>
	import { Router, Route } from "svelte-routing";
    import BigCounter from "./pages/BigCounter.svelte";
    import SmallCounter from "./pages/SmallCounter.svelte";
    import UserCounter from "./pages/UserCounter.svelte";
    import AdminCounter from "./pages/AdminCounter.svelte";
</script>

<Router>
	<div class="container">
		<Route path="/" component={UserCounter} />
        <Route path="/small" component={SmallCounter} />
		<Route path="/big" component={BigCounter} />
        <Route path="/babo" component={AdminCounter} />
	</div>
</Router>

<style>
	main {
		text-align: center;
		padding: 1em;
		margin: 0 auto;
		background-color: #606060;
		min-height: 100vh;
    }
    
    .container{
        margin: 0;
		width: 100%;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-content: center;
		height: 100vh;
		align-items: center;
    }
	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}
	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>