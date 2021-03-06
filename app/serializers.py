from rest_framework import serializers
from app.models import Movie, Rater, Rating

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ["movie_title", "release_date", "video_release_date", "URL", "unknown",
        "Action", "Adventure", "Animation", "Childrens", "Comedy", "Crime", "Documentary",
        "Drama", "Fantasy", "Film_Noir", "Horror", "Musical", "Mystery", "Romance", "Sci_Fi",
        "Thriller", "War", "Western"]


class RaterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rater
        fields = ["age", "gender", "occupation", "zipcode"]


class RatingSerializer(serializers.ModelSerializer):

    user_id = serializers.HyperlinkedRelatedField(
    read_only=True,
    view_name="rater_detail_api_view"
    )

    item_id = serializers.HyperlinkedRelatedField(
    read_only=True,
    view_name="movie_detail_api_view"
    )

    class Meta:
        model = Rating
        fields = ["user_id", "item_id", "rating", "time_stamp"]
