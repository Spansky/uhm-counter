<script>
	import { onMount } from 'svelte';
	let counter = '...';

	async function getCounter() {
        const response = await fetch('http://uhm.codepals.com:8000');
		const json = await response.json();
		return json.counter;
	};
	
	async function incCounter() {
		const response = await fetch('http://uhm.codepals.com:8000/increment', {
			method: 'POST',
			mode: 'cors',
			headers: {
			'Content-Type': 'application/json'
			},
		});
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
