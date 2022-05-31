<script>
    import { Table } from "attractions";
    import { Datatable } from "svelte-simple-datatables";
    import { data } from "./course_table_rows.js";

    const settings = {
        columnFilter: true,
        pagination: false
    };
    let rows;

    // console.log(data);
</script>

<div>
    <!-- <pre>{JSON.stringify(data)}</pre> -->
    <!-- <Datatable {settings} {data} bind:dataRows={rows}>
        <thead>
            <th data-key="n">Number</th>
            <th data-key="t">Title</th>
            <th data-key="c">Credits</th>
        </thead>
        <tbody>
            {#if rows}
            {console.log(data)}
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
    </Datatable> -->
    <!-- <pre>{JSON.stringify(Object.entries(data))}</pre> -->
    <!-- <table>
        <tr>
        <th>Number</th>
        <th>Title</th>
        <th>Credits</th>
        </tr>
        {#each Object.entries(data) as [subject, courses]}
        {console.log(courses)}
            {#each courses as course}
                <tr>
                    <td>{subject}</td>
                    <td>{subject}</td>
                    <td>{subject}</td>
                </tr>
            {/each}
        {/each}
    </table> -->

    <Datatable settings={settings} data={data} bind:dataRows={rows}>
        <thead>
            <th data-key="subject">Subject</th>
            <th data-key="number">Number</th>
            <th data-key="title">Title</th>
            <th data-key="credits">Credits</th>
        </thead>
        <tbody>
            {#if rows}
                {#each $rows as row}
                <tr>
                    <td>{row.s}</td>
                    <td>{row.n}</td>
                    <td>{row.t}</td>
                    <td>{row.c}</td>
                </tr>
                {/each}
            {/if}
        </tbody>
    </Datatable>
</div>

<style>
</style>
