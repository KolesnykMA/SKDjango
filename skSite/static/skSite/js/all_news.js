const button = document.getElementById("load_more_button-all-news");
        const news_list = document.getElementById("news_list");
        let article;
        let num = 3;

        button.addEventListener("click", function () {
        for (let i = 0; i < 4; i++) {
            article = document.getElementsByClassName("news_article")[0].cloneNode(true);
            article.setAttribute("id",+(++num));
            news_list.appendChild(article);
        }
        });