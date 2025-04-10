<template>
  <header>
    <h1>Drowning Statistics</h1>
    <nav>
      <ul>
        <li>
          <router-link to="/">Drowning Search</router-link>
          <router-link to="/BeachData">BeachData</router-link>
        </li>
      </ul>
    </nav>
  </header>
</template>

<script>
export default {
  name: 'BHeader'
};
</script>

<style scoped>
header {
  background-color: #3e8e41;
  color: white;
  padding: 10px;
  text-align: center;
}

nav ul {
  list-style: none;
  padding: 0;
}

nav ul li {
  display: inline;
  margin-right: 20px;
}

nav ul li a {
  color: white;
  text-decoration: none;
  font-size: 18px;
}

nav ul li a:hover {
  text-decoration: underline;
}
</style>
