<script>
	import { onMount } from 'svelte';
	let counter = '...';

	async function getCounter() {
        const response = await fetch('http://uhm.codepals.com:8000');
		const json = await response.json();
		return json.counter;
    };

	onMount(() => {
		const interval = setInterval(() => {
			getCounter().then(data => {counter = data});
		}, 1000);

	return () => {
			clearInterval(interval);
		};
	});

</script>

<p>Uhm-Counter: {counter}</p>

<style>
	p {
		color: rgb(54, 181, 254);
	}
</style>