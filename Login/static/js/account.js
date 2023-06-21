const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

// const SingUp = document.getElementById("SignUp");
// const SignIn = document.getElementById("SignIn");



// signUpButton.addEventListener('click', () => {
  //     location.href = "http://127.0.0.1:8000/login/signup";
  // });
  signUpButton.addEventListener('click', () => {
    container.classList.add("right-panel-active");
  });
  
signInButton.addEventListener('click', () => {
  container.classList.remove("right-panel-active");
});


// $(document).ready(function(){
//   $("form[name=signup]").submit(function(e){
//     // 폼 데이터 가져오기
//     let formData = $(this).serialize();
//     // AJAX 요청 보내기
//     $.ajax({
//       type:'POST',
//       url:'signup/',
//       data:formData,
//       success: function(response){
//         // 성공하였을때 실행되는 코드이다.
//         console.log(response);
        
//       },
//       error: function(xhr, errmsg, err){
//         // 오류를 처리할 코드 
//         console.log(xhr.status + ": " + xhr.responseText);
//       }
//     });
//   });

//   $("form[name=login]").submit(function(e){
      
//     let formData = $(this).serialize(); // 기존의 form 데이터 가져오기
    
//     // AJAX 요청 보내기
//     $.ajax({
//       type: 'POST',
//       url:'login/',
//       data:formData,
//       success: function(response){
//         // 성공하였을때 실행되는 코드이다.
//         console.log(response);
//       },
//       error: function(xhr, errmsg, err){
//         // 오류를 처리할 코드 
//         console.log(xhr.status + ": " + xhr.responseText);
//       }

//     });
//   });

// });

