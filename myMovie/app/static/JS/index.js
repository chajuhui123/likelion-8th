
var key = "?key=3bd0a36fe1ae5e157b1521458a3cb441" // key 앞에 <?key=>를 붙여야함 : prameter // '나는 차주히다! 너의 API를 사용하겠다!'
var itemPerPage = "&itemPerPage=50" // 몇개가져올래!
const url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json"
            + key
            + itemPerPage
            
var item_int = 50
var title = document.getElementById('contents')
var arr = [] ;

fetch(url)
            .then(response=>response.json())
            .then(function(msg){
                for(var i =0; i<item_int; i++){
                    // 사용할 div와 br 태그를 만들었어요!
                    var div = document.createElement('div');
                    var low_div = document.createElement('div');
                    var title_div = document.createElement('div');
                    var br = document.createElement('br'); 

                    // 우리가 가져올 것들에 대해 p태그랑 id를 줄거랍니다.
                    var movieName = document.createElement('p'); // 영화 이름
                    movieName.id = 'movieNmEn'
                    var year = document.createElement('p'); // 제작 연도
                    year.id = 'prdYear'
                    var genre = document.createElement('p'); // 영화 장르
                    genre.id = 'genreAlt'

                    // 각 div에도 아이디를 줄 거에요
                    title_div.id = 'title_div'
                    low_div.id = 'low_div'
                    div.id = 'movies'

                    // 대망의 두근두근 영화 리스트를 가져올거임. 그것도 i 를 for문에 돌려서 하나씩 차곡 차곡.
                    short_url = msg.movieListResult.movieList[i];
                    console.log(short_url);

                    div.appendChild(title_div);
                    div.appendChild(low_div);
                    title.appendChild(div);

                    var movieNmEn = document.createTextNode(short_url.movieNmEn);
                    var prdtYear = document.createTextNode(short_url.prdtYear);
                    var genreAlt = document.createTextNode(short_url.genreAlt);
                    
                    movieName.appendChild(movieNmEn);
                    year.appendChild(prdtYear);
                    genre.appendChild(genreAlt);

                
                    if (short_url.genreAlt == "애니메이션"){
                        arr[i] = [short_url.movieNmEn, short_url.prdtYear, short_url.genreAlt];
                        
                        let nameText = document.createTextNode(short_url.movieNmEn);
                        let yearText = document.createTextNode(short_url.prdtYear);

                        let nameTextBox = document.createElement('div');
                        let yearTextBox = document.createElement('div');

                        contentsBox.appendChild(createDiv).appendChild(nameTextBox).appendChild(nameText);
                        contentsBox.appendChild(createDiv).appendChild(yearTextBox).appendChild(yearText);

                        nameTextBox.setAttribute("class", `nameContents`);
                        yearTextBox.setAttribute("class", `yearContents`);

                        
                        // title_div.appendChild(movieName); 
                        // low_div.appendChild(prdtYear);
                        // low_div.appendChild(genre);
                        // low_div.appendChild(br);

                    }
                }
                        
            });
            console.log(arr);

            

            


            var slideIndex = 0;
            showSlides();
            
            function showSlides() {
                var i;
                var slides = document.getElementsByClassName("mySlides");
                var dots = document.getElementsByClassName("dot");
                for (i = 0; i < slides.length; i++) {
                   slides[i].style.display = "none";  
                }
                slideIndex++;
                if (slideIndex > slides.length) {slideIndex = 1}    
                for (i = 0; i < dots.length; i++) {
                    dots[i].className = dots[i].className.replace(" active", "");
                }
                slides[slideIndex-1].style.display = "block";  
                dots[slideIndex-1].className += " active";
                setTimeout(showSlides, 2000); // Change image every 2 seconds
            }