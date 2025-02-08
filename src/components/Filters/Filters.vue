<template>
  <div class="container">
    <div class="card shadow-sm mb-4">
      <div class="card-header bg-light">
        <h5 class="mb-0">Фильтры</h5>
      </div>
      <div class="card-body">
        <div class="mb-3">
          <label class="form-label">Категория</label>
          <select class="form-select">
            <option value="">Все категории</option>
            <option value="flowers">Цветы</option>
            <option value="bushes">Кустарники</option>
            <option value="trees">Деревья</option>
          </select>
        </div>

        <div class="mb-3">
          <label class="form-label">Размер</label>
          <select class="form-select">
            <option value="">Любой размер</option>
            <option value="small">Маленький</option>
            <option value="medium">Средний</option>
            <option value="large">Большой</option>
          </select>
        </div>

        <div class="mb-3">
          <label class="form-label">Зависимость от солнца</label>
          <select class="form-select">
            <option value="">Любое освещение</option>
            <option value="full-sun">Полное солнце</option>
            <option value="partial-shade">Частичная тень</option>
            <option value="full-shade">Полная тень</option>
          </select>
        </div>

        <div class="mb-3">
          <label class="form-label">Необходимость воды</label>
          <select class="form-select">
            <option value="">Любой режим полива</option>
            <option value="low">Низкая</option>
            <option value="moderate">Умеренная</option>
            <option value="high">Высокая</option>
          </select>
        </div>

        <div class="mb-3">
          <label class="form-label">Сезон</label>
          <select class="form-select">
            <option value="">Любой сезон</option>
            <option value="spring">Весна</option>
            <option value="summer">Лето</option>
            <option value="autumn">Осень</option>
            <option value="winter">Зима</option>
          </select>
        </div>

        <div class="mb-3">
          <label class="form-label">Скорость роста</label>
          <select class="form-select">
            <option value="">Любая скорость</option>
            <option value="slow">Медленная</option>
            <option value="moderate">Умеренная</option>
            <option value="fast">Быстрая</option>
          </select>
        </div>

        <button class="btn btn-secondary w-100">Сбросить фильтры</button>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.container {
    margin-top: 50px;
}
.card-body{
    display: flex !important;
    justify-content: space-between !important;
    flex-wrap: wrap !important;
}
</style>
