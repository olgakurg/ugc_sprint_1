from models import MovieProgress, MovieRes, ClickElement, FilterQuery, PageDuration

kafka_topics = {
    MovieProgress: "movies_progress",
    MovieRes: "movie_resolution",
    ClickElement: "click_element",
    FilterQuery: "filter_query",
    PageDuration: "page_duration",

}
