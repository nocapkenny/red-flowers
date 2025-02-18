<script setup>
const props = defineProps({
  currentPage: {
    type: Number,
    required: true,
  },
  totalPages: {
    type: Number,
    required: true,
  },
});

const emit = defineEmits(["changePage"]);

const changePage = (page) => {
  if (page >= 1 && page <= props.totalPages) {
    emit("changePage", page);
  }
};
</script>

<template>
  <nav aria-label="Page navigation">
    <ul class="pagination">
      <li
        class="page-item"
        v-for="page in totalPages"
        :key="page"
        :class="{ active: page === currentPage }"
      >
        <a class="page-link" href="#" @click.prevent="changePage(page)">{{
          page
        }}</a>
      </li>
    </ul>
  </nav>
</template>

<style lang="scss" scoped>
@use "../../assets/sytles/_vars" as *;

.pagination {
  margin-top: 10px !important;
  margin-bottom: 10px !important;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}
.page-item.active .page-link {
  background-color: $red !important;
  color: $white !important;
  border-color: $red !important;
}
.page-link {
  font-size: 14px !important;
  padding: 5px 10px !important;
  border-radius: 5px;
  border-color: transparent;
}
.page-link:focus {
  box-shadow: none !important;
}
</style>
