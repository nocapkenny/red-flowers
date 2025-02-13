<template lang="pug">
nav(aria-label="Page navigation example", class="navigation example" )
    ul(class="pagination")
        li(class="page-item")
            span
                a(v-on:click="$emit('update:modelValue',modelValue-1)",  v-if="modelValue>1", class="page-link") Назад

        li(v-for="p in maxPage", :key="p.id", class="page-item", v-bind:class="p==modelValue? 'active':''")
            a(v-on:click="$emit('update:modelValue',p)", class="page-link" v-html="p") 
        li(class="page-item")
            span 
                a( @click="$emit('update:modelValue',modelValue+1)", v-if='modelValue>maxPage', class="page-link") Вперед 

</template>
<script>
export default {
    name:'pagination-nav',
    props:['modelValue','maxPage'],
}
</script>
