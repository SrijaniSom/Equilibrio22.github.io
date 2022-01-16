let faq_question = document.getElementsByClassName("faq-question");
let faq_answer = document.getElementsByClassName("faq-answer");
let faq_question_arrow = document.getElementsByClassName("faq-question-arrow");

for (let i = 0; i < faq_question.length; i++) {
    faq_question[i].addEventListener("click", () => {
        closeAll(i);
        if (typeof (faq_question[i].flag) == "undefined" || faq_question[i].flag == 0) {
            faq_question[i].flag = 1;
            faq_answer[i].style.display = "block";
            faq_question[i].style.color = "hsl(237, 12%, 33%)";
            faq_question[i].style.fontWeight = "700";
            faq_question_arrow[i].style.transform = "rotateX(180deg)";
        }
        else {
            closeAll();
        }
    });
}

function closeAll(noTouch) {
    for (let i = 0; i < faq_question.length; i++) {
        if(noTouch != i){
            faq_question[i].flag = 0;
        }
        faq_answer[i].style.display = "none";
        faq_question[i].style.color = "hsl(240, 6%, 50%)";
        faq_question[i].style.fontWeight = "400";
        faq_question_arrow[i].style.transform = "rotateX(0deg)";
    }
}