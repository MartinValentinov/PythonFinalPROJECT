def run_burned(request):
    if request.method == 'POST':
        run  = request.POST['running']

        if run:
            run = float(run)
            if run < 0:
                return render(request)
            run = run // 0.085
            calories = run / 65
            return render(request)
        else:
            error_message = 'Please provide valid kilometers ran'
        
    else:
        return render(request)
    
def walk_burned(request):
    if request.method == 'POST':
        walk = request.POST['walking']

        if walk:
            walk = float(walk)
            if walk > 0:
                walk = walk // 0.05
                calories = walk / 45
                return render(request)
        else:
            error_message = 'Please provide valid kilometers walked'
            messages.error(request, error_message)

    else:
        return render(request)
