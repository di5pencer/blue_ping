# cleans up and returns data from STDOUT
ping_time = 0

def output_parse(text_input):
    while True:
        try:
            out_text1 = text_input.splitlines()[2]
            out_text2 = text_input.splitlines()[1]
            out_text3 = out_text2.split()

        except IndexError:
            break

        while True:
            try:
              ping_time = (out_text3[7])
              return out_text1,ping_time
              break
            except IndexError:
              break
        return out_text1,

#print(output_parse(text1))

