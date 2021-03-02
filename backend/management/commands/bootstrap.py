from django.core.management.base import BaseCommand

from backend.models import (
    User,
    Community,
    CommunityMember,
    Post,
    PostLike,
    PostComment,
    PostCommentLike,
)


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        """
        Command method to handle dummy data creation for testing purposes.
        This command will generate 8 users and ~70 posts with some likes and comments.

        Use after migrating:    python manage.py bootstrap

        Superuser login:
        Email: admin@4ums.com
        Password: admin
        """

        print("Initializing bootstrap...")

        # Admin user.
        admin_user = User.objects.create_user(
            username="admin",
            first_name="Admin",
            last_name="Istrator",
            password="admin",
            email="admin@4ums.com",
            is_staff=True,
            is_superuser=True,
        )

        # Development team accounts!
        sorin = User.objects.create_user(
            username="sorin",
            first_name="Sorin",
            last_name="Burghiu",
            password="sorin",
            email="sorin@4ums.com",
        )
        will = User.objects.create_user(
            username="will",
            first_name="Will",
            last_name="Orringe",
            password="will",
            email="will@4ums.com",
        )
        milo = User.objects.create_user(
            username="milo",
            first_name="Milo",
            last_name="Higgins",
            password="milo",
            email="milo@4ums.com",
        )
        hiba = User.objects.create_user(
            username="hiba",
            first_name="Hiba",
            last_name="AlDalaty",
            password="hiba",
            email="hiba@4ums.com",
        )
        ollie = User.objects.create_user(
            username="ollie",
            first_name="Ollie",
            last_name="Baker",
            password="ollie",
            email="ollie@4ums.com",
        )
        sarah = User.objects.create_user(
            username="sarah",
            first_name="Sarah",
            last_name="Brittain",
            password="sarah",
            email="sarah@4ums.com",
        )
        matt = User.objects.create_user(
            username="matt",
            first_name="Matt",
            last_name="Collison",
            password="matt",
            email="matt@4ums.com",
            is_teacher=True,
        )

        # Create communities.
        team = [sorin, will, milo, hiba, ollie, sarah, matt]
        team_2 = [sorin, will, ollie]
        team_3 = [milo, hiba, sarah]
        ecm2434 = Community.objects.create(
            name="ECM2434", user=matt, description="Cool module."
        )
        chess = Community.objects.create(
            name="Chess",
            user=sorin,
            description="Chess is a recreational and competitive board game played between two players. It is "
            "sometimes called Western or international chess to distinguish it from related games such as "
            "xiangqi. The current form of the game emerged in Southern Europe during the second half of "
            "the 15th century after evolving from similar, much older games of Indian and Persian origin. "
            "Today, chess is one of the world's most popular games, played by millions of people "
            "worldwide at home, in clubs, online, by correspondence, and in tournaments. ",
        )
        for member in team:
            CommunityMember.objects.create(
                user=member,
                community=ecm2434,
            )
        for member in team_2:
            CommunityMember.objects.create(
                user=member,
                community=chess,
            )

        # Create filler posts.
        print("Completed:  5 %")
        count = 1
        for member in team:
            for _ in range(5):
                post = Post.objects.create(
                    user=member,
                    community=ecm2434,
                    title="Lorem ipsum dolor sit amet",
                    description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor "
                    "incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud "
                    "exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure "
                    "dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. "
                    "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt "
                    "mollit anim id est laborum. ",
                    post_type="discussion",
                )
                post_2 = Post.objects.create(
                    user=member,
                    community=ecm2434,
                    title="Lorem ipsum dolor sit amet",
                    description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor "
                                "incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud "
                                "exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure "
                                "dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. "
                                "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt "
                                "mollit anim id est laborum. ",
                    post_type="question",
                )
                for t in team_3:
                    PostLike.objects.create(
                        user=t,
                        post=post,
                    )
                    for i in range(10):
                        if i == 0:
                            comment = PostComment.objects.create(
                                users=t,
                                post=post_2,
                                comment="This is a correct answer.",
                                is_approved=True,
                            )
                        else:
                            comment = PostComment.objects.create(
                                user=t,
                                post=post,
                                comment="Lorem ipsum dolor sit amet",
                            )
                        for t2 in team_2:
                            PostCommentLike.objects.create(
                                user=t2,
                                post_comment=comment,
                            )
            if count < 7:
                print("Completed: ", count * 15 + 5, "%")
                count += 1
        print("Bootstrap completed.")
