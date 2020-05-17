
// https://takeuu.tistory.com/42
// 시계구현
// html요소에서 클래스로 찾아 변수로 등록            
const secondHand = document.querySelector('.second-hand');
const minsHand = document.querySelector('.min-hand');
const hourHand = document.querySelector('.hour-hand');

//시계바늘을 현재 시간에 맞게 설정
function setDate(){
    const now = new Date();

    const seconds = now.getSeconds();
    const secondsDegrees = ((seconds/60)*360)+90;
    secondHand.style.transform = `rotate(${secondsDegrees}deg)`;

    const mins = now.getMinutes();
    const minsDegrees = ((mins/60)*360+(seconds/60)*6) + 90;
    minsHand.style.transform = `rotate(${minsDegrees}deg)`;

    const hour = now.getHours();
    const hourDegrees = ((hour/12)*360+(mins/60)*30) + 90;
    hourHand.style.transform = `rotate(${hourDegrees}deg)`;
    
}
setInterval(setDate,1000);
setDate();

// https://sawol-today.tistory.com/396
// 게임용 1분 타이머 구현
var time = 59;
var min = "";
var sec = "";
document.getElementById("demo").innerHTML = "남은 시간 : "+ 1 + "분" + 00 + "초";
//setInterval(함수,시간) : 주기적인 실행
function timer(){
    min = parseInt(time/60);
    sec = time%60;

    document.getElementById("demo").innerHTML = "남은 시간 : "+ min + "분" + sec + "초";
    time --; // 1초씩 줄어듦

    if (time<0){
        clearInterval(x);
        document.getElementById("demo").innerHTML = "게임종료";
        document.getElementById("modal").style.display="block"; // 모달 팝업
    }
};

// 캐릭터 선택 시 게임화면으로 전환
var imgs = document.getElementsByTagName("img");
for( var x=0; x < 4; x++ ) {
    imgs[x].onclick = function(){
        window.scrollBy({left : 0, top: 1070, behavior:'smooth'});
        setInterval(timer,1000);
        };}
        
//가위바위보 게임
//플레이어 포인트
function Player(p) {
    if (!p) {
        p = 0;
        }
        this.point = p;}

//오버라이딩
Player.prototype.toString = function(){
    switch(this.point){
        case 0 :
        return "가위";
        case 1 :
        return "바위";
        case 2 :
        return "보";
    }
};

//이벤트가 핸들러여서 evt가 넘어옴
var chocobeeSum = 0;
function playerRockScissorsPaper (evt){
    var source = getEventSource(evt); //source는 버튼 element
    var player = new Player();
    var computer = new Player(Math.floor(Math.random()*3)); //0,1,2 발생
    var resultElement = document.getElementById('result'); //이해완료
    var chocobee = document.getElementById('chocobee');

    switch(source.id){
        
        case 'btnScissors':
        player.point = 0;
        break;
        case 'btnRock':
        player.point = 1;
        break;
        case 'btnPaper':
        player.point = 2;
        break;
        default:
        return;
    }
    if(player.point ==computer.point){ //point 같은경우
        resultElement.innerHTML = '비겼습니다';
        chocobee.innerHTML =   chocobeeSum + '개 입니다 ★'; // Q. 이 부분을 사진 및 텍스트로 가능한가?
    } else {
        if((player.point+1)%3 == computer.point){
            resultElement.innerHTML = '졌습니다';
            chocobee =  chocobeeSum+ '개 입니다 ★';
        } else {
            resultElement.innerHTML = '이겼습니다';
            chocobeeSum ++;
            chocobee.innerHTML =  + chocobeeSum + '개 입니다 ★';

            
        }
    };
}

function clearResult() { // 게임 시작 전
    var chocobee = document.getElementById('chocobee');
    var resultElement = document.getElementById("result")
    
    resultElement.innerHTML = "준비"; 
}

function init() {
    var btnRockElement = document.getElementById("btnRock");
    var btnScissorsElement = document.getElementById("btnScissors");
    var btnPaperElement = document.getElementById("btnPaper");
    var btnResetElement = document.getElementById("btnReset");

    addListener(btnRockElement, 'click', playerRockScissorsPaper);
    addListener(btnScissorsElement, 'click', playerRockScissorsPaper);
    addListener(btnPaperElement, 'click', playerRockScissorsPaper);
    addListener(btnResetElement, 'click', clearResult);
    }

//
function addListener(el, ev, handler) {
    
    //크롬 파이어폭스용
    if (el.addEventListener) {//el에 gameElement임
    el.addEventListener(ev, handler, false);
    } else {//익스플로러 8버전 이하용
    el.attachEvent('on' + ev, handler);
    }
    }

//
function getEventSource(evt) {
    //alert(evt.target);//evt.target은 Button엘레먼트
    if (evt.target)
    return evt.target;
    else
    return window.event.srcElement;
    }
addListener(window, 'load', init);
