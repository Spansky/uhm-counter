<script>
	import { onMount } from 'svelte';
	let counter = '...';

	async function getCounter() {
        const response = await fetch('http://localhost:8000');
		const json = await response.json();
		return json.counter;
	};
	
	async function incCounter() {
		const response = await fetch('http://localhost:8000/reset', {
			method: 'POST',
			mode: 'cors',
			headers: {
			'Content-Type': 'application/json'
			},
		});
	}

	onMount(() => {
		const interval = setInterval(() => {
			getCounter().then(data => {counter = data});
		}, 1000);

	return () => {
			clearInterval(interval);
		};
	});

</script>

<style>
	button {
		font-size: 300px;  
		color: rbg(54,181,254);
	}
</style>

<div>
	<button on:click={incCounter}>{counter}</button>
</div>
