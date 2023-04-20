if __name__ == '__main__':
    from termcolor import cprint
    import sys
    if len(sys.argv) != 2:
        print('\n')
        cprint('> Usage: python3 run.py [PORT]', 'cyan')
        print('\n')
        exit()
    port = int(sys.argv[1])
    cprint(f"""
    ██████╗░██████╗░░█████╗░████████╗░█████╗░███╗░░██╗
    ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗████╗░██║
    ██████╔╝██████╔╝██║░░██║░░░██║░░░██║░░██║██╔██╗██║
    ██╔═══╝░██╔══██╗██║░░██║░░░██║░░░██║░░██║██║╚████║
    ██║░░░░░██║░░██║╚█████╔╝░░░██║░░░╚█████╔╝██║░╚███║
    ╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚══╝""", 'cyan')
    cprint('                             {}'.format(port), 'magenta')
    from src.routes import app
    app.run(host='127.0.0.1', port=port)
