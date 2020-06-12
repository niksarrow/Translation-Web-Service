from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem, UnmtItem
import subprocess, os
from subprocess import check_output, STDOUT, CalledProcessError
# Create your views here.

def yourName(request):
    all_todo_items = TodoItem.objects.all()
    current_name = "Nikhil Saini"
    return render(request, 'todo.html', {'all_items' : all_todo_items, 'current_name' : current_name})

def myView(request):
    return HttpResponse("Hello!! I'm Translation.")

def pageView(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, 'todo.html', {'all_items' : all_todo_items})

def addTodo(request):
    c = request.POST['content']
    new_item = TodoItem(content = c)
    new_item.save()
    return HttpResponseRedirect('/index/')
    # create a new todo item and save it
    # save it
    # redirect the browser to /page/

def deleteAll(request):
    # c = request.POST['todo_id']
    TodoItem.objects.all().delete()
    return HttpResponseRedirect('/index/')

def deleteAllUnmt(request):
    # c = request.POST['todo_id']
    UnmtItem.objects.all().delete()
    return HttpResponseRedirect('/index/')

def deleteTodo(request, todo_id):
    # c = request.POST['todo_id']
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/index/')

def deleteUnmt(request, unmt_id):
    # c = request.POST['todo_id']
    item_to_delete = UnmtItem.objects.get(id=unmt_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/index/')

def translate(request):
    c = request.POST['source_sent']
    cmd = r"../seminar/iwslt_2020/"
    # print(os.getcwd())
    os.chdir(cmd)
    # print(os.getcwd())
    os.chdir("web_service")
    cmd = 'echo "{0}" > test.es'.format(c)
    os.system(cmd)
    os.chdir("../")
    cmd = r"./get_data_esen_noise_web_service.sh"
    try:
        check_output(cmd, shell=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        #os.chdir("-")
        raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
    # cwd = os.getcwd()
    # print(cwd)
        
    cmd = r"python3 main.py --exp_name 'webservice' --transformer 'True' --n_enc_layers '4' --n_dec_layers '4' --share_enc '3' --share_dec '3' --share_lang_emb 'True' --share_output_emb 'True' --emb_dim '512' --langs 'en,es'  --para_dataset 'en-es:./web_service/train.XX.tok.50000.pth,./web_service/tun.XX.tok.50000.pth,./web_service/test.XX.tok.50000.pth' --para_directions 'en-es,es-en' --n_para '-1' --lambda_xe_para '1' --pretrained_emb './data/noise1/mono/all.es-en.50000.vec' --dropout '0.3' --label-smoothing '0.1' --eval_only 'True' --reload_model './web_service/iwslt_mid.pth' --reload_enc 'True' --reload_dec 'True' --group_by_size 'False' --is_web_service 'True'"
    try:
        check_output(cmd, shell=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))

    os.chdir("web_service")
    gen = open('gen.txt', 'r').readlines()[0]
    os.chdir("../../../Translation-Web-Service")
    new_item = TodoItem(content = c, gen = gen)
    new_item.save()
    all_todo_items = TodoItem.objects.all()
    all_unmt_items = UnmtItem.objects.all()
    return render(request, 'index.html', {'all_items' : all_todo_items, 'all_unmt_items' : all_unmt_items, 'gen' : gen, 'source' : c})

def translateUnmt(request):
    c = request.POST['source_sent_unmt']
    gen = c + " unmt"
    # generate here
    new_item = UnmtItem(content = c, gen = gen)
    new_item.save()
    all_todo_items = TodoItem.objects.all()
    all_unmt_items = UnmtItem.objects.all()
    return render(request, 'index.html', {'all_items' : all_todo_items, 'all_unmt_items' : all_unmt_items, 'gen_unmt' : gen, 'source_unmt' : c})

def index(request):
    all_todo_items = TodoItem.objects.all()
    all_unmt_items = UnmtItem.objects.all()
    return render(request, 'index.html', {'all_items' : all_todo_items,'all_unmt_items' : all_unmt_items})
    # return render(request, 'index.html')

def wix(request):
    return render(request, 'wix.html')
