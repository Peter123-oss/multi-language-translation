const ip = 'http://localhost:5000/';

export default {
  user:{
    login:ip+'user/login',
    register:ip+'user/register'
  },
  school:{
    addschool:ip+'school/addschool',
    schoollist:ip+'school/schoollist',
    allschool:ip+'school/allschool'
  }
};