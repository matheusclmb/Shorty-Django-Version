from rest_framework import serializers

from shorty.models import Shortener


class StatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shortener
        fields = ("startDate", "lastSeenDate", "redirectCount", "url", "shortcode")


class ShortenerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shortener
        fields = ("url", "shortcode")
