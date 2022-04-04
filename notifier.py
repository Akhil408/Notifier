from plyer import notification

title = 'Hello Akhil Rajput'
message= 'You have studied for 1hr ,Take a break and play BGMI'

notification.notify(title= title,
                    message= message,
                    app_icon = None,
                    timeout= 10,
                    toast=False)
