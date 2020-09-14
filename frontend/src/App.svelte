<script>
	import { onMount } from 'svelte';
	let counter = [];

	onMount(async function() {
        const response = await fetch('http://localhost:8000');
		counter = await response.json();
    });
	

	// onMount(() => {
	// 	const interval = setInterval(() => {
	// 		counter = fetchCounter();
	// 	}, 1000);

	// return () => {
	// 		clearInterval(interval);
	// 	};
	// });

</script>

<main>
	<p>Uhm-Counter: {counter.counter}</p>
</main>

<style>
	p {
		color: red;
	}
</style>