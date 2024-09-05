// Function to run when the page loads
var email = document.getElementById("email").value;

function onPageLoad() {
    var email = document.getElementById("email").value;
    $.ajax({
        url: `/dashboard/course/${email}`,
        type: "POST",
        success: function (response) {
            videodiv = document.getElementById("VideoOrQuiz");
            if (response.quiz == 0){
                videodiv.innerHTML = `
                   <div id="video-section" class="pt-2">
                    <video id="video-player" controls>
                    <source src="../static/videos/${response.State}.mp4" type="video/mp4" autoplay>
                    </video>
                    </div>
                `;
                console
                IncrementState(email);
            }
            else{
                videodiv.innerHTML = `
                    <div id="quiz-section" class="pt-5">
                    <h2>${response.Question}</h2>
                    <div class="quiz-options">
                    <button onclick="ShowCorrect(${response.Option1})>${response.Option1}</button>
                    <button onclick="ShowCorrect(${response.Option2})>${response.Option2}</button>
                    <button onclick="ShowCorrect(${response.Option3})>${response.Option3}</button>
                    <button id="Correctanswer" class="hidden" style="border:green 5px solid;">${response.Answer}</button>
                    </div>
                    </div>
                `;
            }
        },
        error: function (error) {
          console.log("error: ", error);
        }
      });    
}
window.onload = onPageLoad;

function IncrementState(email){
    $.ajax({
        url: `/dashboard/IncrementState/${email}`,
        type: "POST",
        data:{

        },
        success: function (response) {
            console.log("State Incremented");
        },
        error: function (error) {
          console.log("error: ", error);
        }
      }); 
}

function ShowCorrect(realans){
    const correctAnswer = document.getElementById("Correctanswer").value;
    const email = document.getElementById("email").value;
    correctAnswer.className = ""
    if (correctAnswer == realans){
        IncrementState(email);
    }
}