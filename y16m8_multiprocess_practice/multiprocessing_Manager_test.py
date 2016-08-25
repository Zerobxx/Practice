from multiprocessing import Process, Value, Array, Manager

g_value = Value('i', 0)
g_array = Array('i', range(10))
g_manager = Manager()
g_dict = g_manager.dict()

print 'init g_value = %d\ninit g_array = %s\ninit g_dict = %s' %(g_value.value, g_array[:], g_dict)

def child_func(g_value, g_array, g_dict, i):
    print 'in child', i
    g_value.value = i
    g_array[i] = i*i
    g_dict[i] = i+i
    print 'g_value =', g_value.value

sub_process_list = []

for i in range(10):
    p = Process(target= child_func, args=(g_value, g_array, g_dict, i))
    p.start()
    sub_process_list.append(p)

for i in range(10):
    sub_process_list[i].join()

print g_value.value
print g_array[:]
print g_dict

