def concatenate(*args, **kwargs):
        text = "".join(args)
        for key in kwargs:
            text = text.replace(key, kwargs[key])
        return text


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))