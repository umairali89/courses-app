import graphene
from graphene_django import DjangoObjectType
from graphene_django import DjangoListField
from .models import Quizzes, Category, Question, Answer


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name")


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("title", "quiz")


class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ("question", "answer_text")


class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = ("id", "title", "category", "quiz")


class Query(graphene.ObjectType):

    # all_quizzes = DjangoListField(QuizzesType)
    all_quizzes = graphene.Field(QuizzesType, id=graphene.Int())
    all_category = DjangoListField(CategoryType)
    all_questions = graphene.Field(QuestionType, id=graphene.Int())
    all_answer = graphene.List(AnswerType, id=graphene.Int())

    def resolve_all_quizzes(root, info, id):
        # return Quizzes.objects.all()
        return Quizzes.objects.get(pk=id)

    def resolve_all_questions(root, info, id):
        return Question.objects.get(pk=id)

    def resolve_all_answer(root, info, id):
        return Answer.objects.filter(question=id)

    def resolve_all_category(root, info):
        return Category.objects.all()


class CategoryMutation(graphene.Mutation):

    class Arguments:
        id = graphene.ID()
        # name = graphene.String(required=True)

    category = graphene.Field(CategoryType)

    @classmethod
    # def mutate(cls, root, info, id):
    def mutate(cls, root, info, id):
        category = Category.objects.get(id=id)
        # category.name = name
        # category.save()
        category.delete()
        # return CategoryMutation(category=category)
        return


class Mutation(graphene.ObjectType):

    update_category = CategoryMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
