<script>
	import { onMount } from 'svelte';
	let counter = '...';

	async function getCounter() {
        const response = await fetch('https://uhm-counter-2.azurewebsites.net/api/uhm-counter');
		const json = await response.json();
		return json.counter;
    };

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
	p {
		font-size: 300px;  
		color: rgb(54, 181, 254);
	}
</style>

<p>{counter}</p>