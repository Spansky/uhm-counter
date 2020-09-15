<script>
	import { onMount } from 'svelte';
	let counter = '...';

	async function getCounter() {
        const response = await fetch('https://uhm-counter-2.azurewebsites.net/api/uhm-counter');
		const json = await response.json();
		return json.counter;
	};
	
	async function incCounter() {
		const response = await fetch('https://uhm-counter-2.azurewebsites.net/api/uhm-counter-increase');
		counter = counter +1;
	}

	onMount(() => {
		const interval = setInterval(() => {
			getCounter().then(data => {counter = data});
		}, 5000);

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
