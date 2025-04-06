<template>
    <div>
      <Bar :data="chartData" :options="chartOptions" />
    </div>
  </template>
  
  <script>
  import { Bar } from 'vue-chartjs'
  import {
    Chart as ChartJS,
    Title,
    Tooltip,
    Legend,
    BarElement,
    CategoryScale,
    LinearScale
  } from 'chart.js'
  import ChartDataLabels from 'chartjs-plugin-datalabels'
  
  ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale, ChartDataLabels)
  
  export default {
    components: { Bar },
    props: {
      chartData: { type: Object, required: true }
    },
    computed: {
      chartOptions() {
        return {
          responsive: true,
          plugins: {
            legend: { position: 'top' },
            title: {
              display: true,
              text: 'Beach Comparison Chart'
            },
            datalabels: {
              anchor: 'end',
              align: 'top',
              formatter: (value) => {
                if (typeof value === 'number') {
                  return value.toFixed(2)
                }
                return value
              },
              color: '#000',
              font: {
                weight: 'bold'
              }
            }
          },
          scales: {
            y: {
              beginAtZero: true
            }
          }
        }
      }
    }
  }
  </script>
  