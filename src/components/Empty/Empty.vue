<template>
  <div class="empty">
    <p class="empty__text">
      Похоже, что ничего не нашлось или вы не выбрали фильтры 🌳
    </p>
  </div>
</template>

<style lang="scss" scoped>
@use "../../assets/sytles/_mixins" as *;
.empty {
  @include content-box();
  width: 100%;
  padding-top: 20px;
  &__text {
    font-size: 24px;
    text-align: center;
    @media (min-width: 600px) {
      font-size: 32px;
    }
  }
}
</style>
