import cloudconvert 


API_KEY = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiMmQ3ZGViNjA0MTMyM2Y3MzNjYTFlNWVmOTg3NThlZmQ2OTU2Y2NlMjZjOTY4Yjc0ZGU0Mjc5NDgwYWM1NmJmOWJlMTcwYjEwMjU3NzNiYTgiLCJpYXQiOjE2NTA0Njk5ODcuNzk4NDIyLCJuYmYiOjE2NTA0Njk5ODcuNzk4NDI0LCJleHAiOjQ4MDYxNDM1ODcuNzg2MjU1LCJzdWIiOiI1NzQ2NjgwNyIsInNjb3BlcyI6WyJ1c2VyLnJlYWQiLCJ1c2VyLndyaXRlIiwidGFzay5yZWFkIiwidGFzay53cml0ZSIsIndlYmhvb2sucmVhZCIsIndlYmhvb2sud3JpdGUiLCJwcmVzZXQucmVhZCIsInByZXNldC53cml0ZSJdfQ.k2C9tmbgODWsadJAQqlxnsj6595A-cLLCHYl17V72gZPSXOy3-nklV91r5e2NPHqTtOb6m4-R1kPwWu6FZdHA9xAcQVefEr9xyT1TicmAUh17w93FeNr5M7giIctIwvuRZ4wXYy3WMuFXi40e2lqUsJ-MEz6nJRLpLNUgOIG1SrjFx0l3Jk2sdXFIQqRTdgx1Ii-a_-TloCebrYsUKOsKxkdlo0S4BG4UajAwPQxVtGV6uSCesRQtgx8UsxB1MLz9dbA5NQAToUvMg4eg3_lRcyidaIxWplwVBrL9BMJUpaB9IAzktcFNO4sKYMLGLZBgUD-oMEujv4mVj07lG4CmwLGe_WUmT_Yevz8maEc3oJz9DGAwJIycK-E-QQhgTd1BLXAO5Z16h38Ss0Cjng23o0k-GRO15IUVAff3VzCcOJ5zb3MbEMxUSymhxEgmx93vNuFyxCGqg2Gg106kHw2Bg9nw6KqvkZJfvxAkYcEPTBCGk8_iJABeqCB7njvMJsXP83bZY-3lHYQ5yBdaJGiL62cdXY9zP9vyYT7TTNGxYwWUoECqqCVREC3ogKBaOG1zpQ0V0CSpSkaRjRYxzszJRanXEuEp_rCI0ewowkOL0yFFhqUXfebEZZ9ppsqOHLsD0vwFk5gcsr4b2Uwis5s_DWH9nirjzZb1siVg-XwJxk'
cloudconvert.configure(api_key=API_KEY, sandbox=False)

cloudconvert.Job.create(payload={
    "tasks": {
        'import-my-file': {
            'operation': './chi.txt',
            
        },
        'convert-my-file': {
            'operation': 'convert',
            'input': 'import-my-file',
            'output_format': 'pdf',
            'some_other_option': 'value'
        },
        'export-my-file': {
            'operation': 'export/url',
            'input': 'convert-my-file'
        }
    }
})

exported_url_task_id = "84e872fc-d823-4363-baab-eade2e05ee54"
res = cloudconvert.Task.wait(id=exported_url_task_id)  # Wait for job completion
file = res.get("result").get("files")[0]
res = cloudconvert.download(filename=file['filename'], url=file['url'])
print(res)