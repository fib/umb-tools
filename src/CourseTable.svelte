<script>
    import { Table } from "attractions";
    import { Datatable } from "svelte-simple-datatables";
    import * as data from "./course_catalog.json";

   

    const settings = {
        columnFilter: true,
        css: false,
        pagination: false
    };
    let rows;

    console.log(data);
</script>

<div>
    <!-- <pre>{JSON.stringify(data)}</pre> -->
    <Datatable {settings} {data} bind:dataRows={rows}>
        <thead>
            <th data-key="n">Number</th>
            <th data-key="t">Title</th>
            <th data-key="c">Credits</th>
        </thead>
        <tbody>
            {#if rows}
                {#each Object.entries(data) as [subject, courses]}
                    {#each courses as course}
                    <tr>
                        <td>{course.first_name}</td>
                        <td>{course.last_name}</td>
                        <td>{course.email}</td>
                    </tr>
                    {/each}
                {/each}
            {/if}
        </tbody>
    </Datatable>
</div>

<style>
</style>
