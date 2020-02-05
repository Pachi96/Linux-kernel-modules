#include <linux/module.h>
#include <linux/ptrace.h>
#include <linux/init.h>
#include <linux/input.h>
#include <linux/io.h>

#include <asm/hardware/iomd.h>

static struct input_dev *vmaus_dev;

int ms_open(struct inode *pinode, struct file *pfile)
{
return 0;
}

void move_cursor(int dx, int dy)
{
input_report_rel(vmaus_dev, REL_X, dx);
input_report_rel(vmaus_dev, REL_Y, dy);
input_sync(vmaus_dev);
}

ssize_t ms_read(struct file *pfile, char __user *buffer, size_t length, loff_t *offset)
{
//move the mouse up and right
move_cursor(10,-10);
return 0;
}

ssize_t ms_write(struct file *pfile, const char __user *buffer, size_t length, loff_t *offset)
{
//move the mouse up and left
move_cursor(-10,-10);
return length;
}

int ms_close(struct inode *pinode, struct file *pfile)
{
return 0;
}

struct file_operations ms_file_operations = {
.owner    = THIS_MODULE,
.open     = ms_open,
.read     = ms_read,
.write    = ms_write,
.release  = ms_close,
};


static int __init vmaus_init(void)
{
	int error;

	register_chrdev(238, "mausvv", &ms_file_operations);
	vmaus_dev = input_allocate_device();

	vmaus_dev->name = "Alfonso's virtual mouse";
	vmaus_dev->id.bustype = BUS_HOST;

	vmaus_dev->evbit[0] = BIT_MASK(EV_KEY) | BIT_MASK(EV_REL);

	vmaus_dev->keybit[BIT_WORD(BTN_LEFT)] = BIT_MASK(BTN_LEFT) |
		BIT_MASK(BTN_MIDDLE) | BIT_MASK(BTN_RIGHT);

	vmaus_dev->relbit[0]	= BIT_MASK(REL_X) | BIT_MASK(REL_Y);

	error = input_register_device(vmaus_dev);
	printk(KERN_ALERT "Virtual mouse initialized");
	return 0;
}

static void __exit vmaus_exit(void)
{
	input_unregister_device(vmaus_dev);
	unregister_chrdev(238, "mausvv");
	printk(KERN_ALERT "Virtual mouse stopped");
}

module_init(vmaus_init);
module_exit(vmaus_exit);
