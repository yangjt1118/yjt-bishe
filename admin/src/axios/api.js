import axios from 'axios'

axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded'

// 请求拦截器

axios.interceptors.request.use(function(config) {

    return config;

  }, function(error) {

    return Promise.reject(error);

  })
// axios.interceptors.request.use(
//     config => {
//       if (localStorage.getItem('Authorization')) {
//         config.headers.Authorization = localStorage.getItem('Authorization');
//       }
   
//       return config;
//     },
//     error => {
//       return Promise.reject(error);
//     });

  // 响应拦截器

axios.interceptors.response.use(function(response) {

  return response;

}, function(error) {

      return Promise.reject(error);

})

// 封装axios的post请求

export function fetch(url, params) {

      return new Promise((resolve, reject) => {

        axios.post(url, params)

          .then(response => {

            resolve(response.data);

      })

      .catch((error) => {

            reject(error);

      })

  })

}

export default {

          mockdata(url, params) {

            return fetch(url, params);

  }

}