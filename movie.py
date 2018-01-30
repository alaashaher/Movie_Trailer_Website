import fresh_tomatoes
import video

# toy story: movie title, story line, poster image and movie trailer
toy_story = video.Video_(
    "toy story",
    "story of a boy and his toys that come to life",
    "http://imgsrc.allposters.com/img/print/posters/toy-story"
    "-3-gang_a-G-8709720-0.jpg",  # NOQA
    "https://www.youtube.com/watch?v=KYz2wyBy3kc"
    )

# Avatar: movie title, story line, poster image and movie trailer
avatar = video.Video_(
    "Avatar",
    "A marine on an alien planet",
    "https://upload.wikimedia.org/wikipedia/en/"
    "b/b0/Avatar-Teaser-Poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=cX0R3mXaod8"
    )

# Up: movie title, story line, poster image and movie trailer
up = video.Video_(
    "Up",
    "Carl Fredricksen (Ed Asner),a 78-year-old"
    " balloon salesman, is about to fulfilla lifelong dream."
    "Tying thousands of balloons to his house,"
    " he flies away to the South"
    "American wilderness. But curmudgeonly Carl's"
    " worst nightmare comes true when he discovers"
    "a little boy named Russell is a stowaway aboard"
    " the balloon-powered house.",  # NOQA
    "https://lumiere-a.akamaihd.net/v1/images/"
    "open-uri20150422-12561-17yo1p6_142a7bbd.jpeg",
    "https://www.youtube.com/watch?v=VR8hlvLghrs"
    )

# School Of Rock: movie title, story line, poster image and movie trailer
school_of_rock = video.Video_(
    "School of rock",
    " Overly enthusiastic guitarist Dewey "
    " Finn (Jack Black) gets thrown out of his bar band "
    "and finds himself in desperate need of work"
    ". Posing as a substitute music teacher at an "
    "elite private elementary school, he exposes "
    "his students to the hard rock gods he idolizes and emulates"
    "-- much to the consternation of the uptight principal (Joan Cusack)."
    "As he gets his privileged and precocious "
    "charges in touch with their inner rock 'n' "
    "roll animals, he imagines redemption at a local Battle of the Bands.",
    "https://static.independent.co.uk/s3fs-public/"
    "thumbnails/image/2016/05/09/16/school-of-rock.jpg",  # NOQA
    "https://www.youtube.com/watch?v=oP7kExN8LFA"
    )

# Ratatouille: movie title, story line, poster image and movie trailer
ratatouille = video.Video_(
    "Ratatouille",
    "Remy (Patton Oswalt), a resident of Paris, appreciates good food and has"
    "quite a sophisticated palate. He would love to"
    " become a chef so he can create"
    " and enjoy culinary masterpieces to his heart's"
    " delight. The only problem is, Remy is a rat. "
    "When he winds up in the sewer beneath one of Paris' finest restaurants, "
    "the rodent gourmet finds himself ideally placed to realize his dream",
    "http://www.gstatic.com/tv/thumb/dvdboxart"
    "/165058/p165058_d_v8_aa.jpg",  # NOQA
    "https://www.youtube.com/watch?v=c3sBBRxDAqk"
    )

# Hunger Games: movie title, story line, poster image and movie trailer
hunger_games = video.Video_(
    "Hunger Games",
    "In what was once North America, the Capitol"
    " of Panem maintains its hold on its 12 districts "
    "by forcing them each to select a boy and a girl,"
    " called Tributes, to compete in a nationally "
    "televised event called the Hunger Games. Every"
    " citizen must watch as the youths fight to the "
    "death until only one remains. District 12 "
    "Tribute Katniss Everdeen "
    "(Jennifer Lawrence) has little to rely on, "
    "other than her hunting skills "
    "and sharp instincts, in an arena where she"
    " must weigh survival against love.",
    "http://dekhnews.com/wp-content/uploads/2015/07"
    "/Hollywood-Movie-The-Hunger-Games-New-Trailer-Video-Released.jpg",  # NOQA
    "https://www.youtube.com/watch?v=PbA63a7H0bo"
    )

# to open the website
movies = [toy_story, avatar, up, school_of_rock, ratatouille, hunger_games]
fresh_tomatoes.open_movies_page(movies)
