// Function to run when the page loads
// var email = document.getElementById("email").value;

function onPageLoad() {
    var email = document.getElementById("email").value;
    $.ajax({
        url: `/dashboard/course/${email}`,
        type: "POST",
        success: function (response) {
            videodiv = document.getElementById("VideoOrQuiz");
            if (response.quiz == 0){
                videodiv.innerHTML = `
                    <video width="100%" height="100%" controls autoplay loop muted poster="poster-image.jpg">
                    <source src="${response.State}.mp4" type="video/mp4">
                    </video>
                `;
                console
                IncrementState(email);
            }
            else{
                videodiv.innerHTML = `
                    
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
        success: function (response) {
            console.log("State Incremented");
        },
        error: function (error) {
          console.log("error: ", error);
        }
      }); 
}