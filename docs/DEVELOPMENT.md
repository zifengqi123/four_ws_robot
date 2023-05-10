определяем переменную `CATKIN_WORKSPACE`

```bash
echo "export CATKIN_WORKSPACE="$HOME/catkin_ws"" >> ~/.zshrc
```

установка требуемых пакетов

```bash
cd $CATKIN_WORKSPACE/src/four_ws_robot/third_party
```

```bash
./install_third_party.sh
```