<script>
import { ContentLoader } from "vue-content-loader";

export default {
  components: { ContentLoader },
};
</script>

<template>
  <content-loader
    viewBox="0 0 280 520"
    :speed="3"
    primaryColor="#eee3e3"
    secondaryColor="#fb8383"
    class="skeleton"
  >
    <rect x="0" y="465" rx="3" ry="3" width="275" height="40" />
    <rect x="0" y="436" rx="3" ry="3" width="300" height="8" />
    <rect x="0" y="393" rx="3" ry="3" width="300" height="20" />
    <rect x="0" y="2" rx="20" ry="20" width="280" height="380" />
    <rect x="0" y="447" rx="3" ry="3" width="300" height="7" />
  </content-loader>
</template>

<style lang="scss" scoped>
@use "../../assets/sytles/_vars" as *;
.skeleton {
  background-color: $white;
  box-shadow: $shadow;
  border-radius: 20px;
  height: 100%;
  cursor: pointer;
  max-width: 310px;
}
.skeleton + .skeleton {
  margin-left: 20px;
}
</style>
