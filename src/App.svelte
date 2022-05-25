<script>
	import { H1 } from 'attractions';
	import CourseTable from './CourseTable.svelte';

</script>

<main>
	<H1>UMB Course Catalog</H1>

	<CourseTable/>
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>