"""Farm DB layer using Peewee ORM (SQLite). Type-safe edition."""

from __future__ import annotations

from datetime import date, datetime
from pathlib import Path
from typing import Any, Literal, TypedDict, cast

from peewee import (
    AutoField,
    BooleanField,
    CharField,
    DateTimeField,
    FloatField,
    IntegerField,
    Model,
    SqliteDatabase,
)

DB_PATH = Path(__file__).parent / "farm.db"

db = SqliteDatabase(str(DB_PATH))

# ---- Constrained vocabularies (UI + seeds use these) ----
CropStatus = Literal["Зростає", "Зібрано", "Заплановано", "Втрачено"]
HealthStatus = Literal["Здорова", "Хвора", "Потребує огляду", "На лікуванні"]
AnimalTypeName = Literal["Корова", "Вівця", "Коза", "Свиня", "Курка", "Кінь", "Інше"]
TaskCategory = Literal["Загальне", "Посіви", "Тварини", "Запаси", "Обслуговування"]
TaskPriority = Literal["Низький", "Середній", "Високий"]
InventoryCategory = Literal[
    "Ручні інструменти",
    "Електроінструменти",
    "Техніка",
    "Запчастини",
    "Паливо",
    "Добрива",
    "Насіння",
    "Корми",
    "Інше",
]
InventoryCondition = Literal["Справний", "Потребує ремонту", "Зламаний"]
InventoryUnit = Literal["шт", "кг", "л", "м", "компл."]
LogEntity = Literal["Посіви", "Тварини", "Завдання", "Інвентар"]
LogAction = Literal["Створено", "Оновлено", "Видалено", "Перемкнуто"]

CROP_STATUSES: tuple[CropStatus, ...] = (
    "Зростає",
    "Зібрано",
    "Заплановано",
    "Втрачено",
)

# Streamlit widgets hand us `str`, `date`, or None — normalize at the boundary.
DateInput = str | date | datetime | None
TextInput = str | None
NumberInput = float | int | str | None


class CropRecord(TypedDict):
    id: int
    name: str
    variety: str
    field: str
    area_ha: float
    plant_date: str
    harvest_date: str
    status: str
    notes: str


class AnimalRecord(TypedDict):
    id: int
    animal_type: str
    tag_id: str
    breed: str
    birth_date: str
    health_status: str
    notes: str


class TaskRecord(TypedDict):
    id: int
    title: str
    category: str
    due_date: str
    priority: str
    done: bool
    notes: str


class InventoryRecord(TypedDict):
    id: int
    name: str
    category: str
    quantity: float
    unit: str
    condition: str
    location: str
    notes: str


class LogRecord(TypedDict):
    id: int
    created_at: str
    entity: str
    action: str
    entity_id: int | None
    details: str


def _s(value: TextInput, default: str = "") -> str:
    return value if isinstance(value, str) else default


def _d(value: DateInput) -> str:
    if value is None:
        return ""
    return value.isoformat() if isinstance(value, (date, datetime)) else str(value)


def _f(value: NumberInput, default: float = 0.0) -> float:
    try:
        return float(value or 0)
    except (TypeError, ValueError):
        return default


class BaseModel(Model):
    class Meta:
        database = db

    def to_dict(self) -> dict[str, Any]:
        return dict(self.__data__)


class Crop(BaseModel):
    class Meta:
        table_name = "crops"

    id = AutoField()
    name = CharField(default="")
    variety = CharField(default="")
    field = CharField(default="")
    area_ha = FloatField(default=0)
    plant_date = CharField(default="")
    harvest_date = CharField(default="")
    status = CharField(default="Зростає")
    notes = CharField(default="")


class Animal(BaseModel):
    class Meta:
        table_name = "livestock"

    id = AutoField()
    animal_type = CharField(default="")
    tag_id = CharField(default="")
    breed = CharField(default="")
    birth_date = CharField(default="")
    health_status = CharField(default="Здорова")
    notes = CharField(default="")


class Task(BaseModel):
    class Meta:
        table_name = "tasks"

    id = AutoField()
    title = CharField(default="")
    category = CharField(default="Загальне")
    due_date = CharField(default="")
    priority = CharField(default="Середній")
    done = BooleanField(default=False)
    notes = CharField(default="")


class InventoryItem(BaseModel):
    class Meta:
        table_name = "inventory"

    id = AutoField()
    name = CharField(default="")
    category = CharField(default="Інше")
    quantity = FloatField(default=0)
    unit = CharField(default="шт")
    condition = CharField(default="Справний")
    location = CharField(default="")
    notes = CharField(default="")


class ActivityLog(BaseModel):
    class Meta:
        table_name = "activity_log"

    id = AutoField()
    created_at = DateTimeField(default=datetime.now)
    entity = CharField(default="")
    action = CharField(default="")
    entity_id = IntegerField(null=True)
    details = CharField(default="")


def _log(
    entity: str, action: str, entity_id: int | None = None, details: str = ""
) -> None:
    try:
        ActivityLog.create(
            entity=entity, action=action, entity_id=entity_id, details=details or ""
        )
    except Exception:
        pass


def init_db() -> None:
    db.connect(reuse_if_open=True)
    db.create_tables([Crop, Animal, Task, InventoryItem, ActivityLog])
    _migrate_en_to_uk()
    _seed_if_empty()


def _migrate_en_to_uk() -> None:
    """One-time migration of old English values to Ukrainian."""
    en_to_uk = {
        "Growing": "Зростає",
        "Harvested": "Зібрано",
        "Planned": "Заплановано",
        "Failed": "Втрачено",
        "Healthy": "Здорова",
        "Sick": "Хвора",
        "Needs check": "Потребує огляду",
        "In treatment": "На лікуванні",
        "General": "Загальне",
        "Crops": "Посіви",
        "Livestock": "Тварини",
        "Supplies": "Запаси",
        "Maintenance": "Обслуговування",
        "Low": "Низький",
        "Medium": "Середній",
        "High": "Високий",
        "Cow": "Корова",
        "Sheep": "Вівця",
        "Goat": "Коза",
        "Pig": "Свиня",
        "Chicken": "Курка",
        "Horse": "Кінь",
        "Other": "Інше",
        "Wheat": "Пшениця",
        "Corn": "Кукурудза",
        "Potatoes": "Картопля",
        "Winter Red": "Озима червона",
        "Sweet Gold": "Цукрова золота",
        "Russet": "Рассет",
        "North field": "Північне поле",
        "South field": "Південне поле",
        "East field": "Східне поле",
        "Needs irrigation": "Потребує поливу",
        "Laying group": "Несуча група",
        "Limping slightly": "Злегка кульгає",
        "Irrigate south field": "Полити південне поле",
        "Vet check for S-050": "Ветогляд S-050",
        "Order feed": "Замовити корм",
    }
    for en, uk in en_to_uk.items():
        Crop.update(status=uk).where(Crop.status == en).execute()
        Crop.update(name=uk).where(Crop.name == en).execute()
        Crop.update(variety=uk).where(Crop.variety == en).execute()
        Crop.update(field=uk).where(Crop.field == en).execute()
        Crop.update(notes=uk).where(Crop.notes == en).execute()
        Animal.update(animal_type=uk).where(Animal.animal_type == en).execute()
        Animal.update(health_status=uk).where(Animal.health_status == en).execute()
        Animal.update(notes=uk).where(Animal.notes == en).execute()
        Task.update(title=uk).where(Task.title == en).execute()
        Task.update(category=uk).where(Task.category == en).execute()
        Task.update(priority=uk).where(Task.priority == en).execute()


def _seed_if_empty() -> None:
    if not Crop.select().exists():
        Crop.insert_many(
            [
                {
                    "name": "Пшениця",
                    "variety": "Озима червона",
                    "field": "Північне поле",
                    "area_ha": 12.5,
                    "plant_date": "2026-03-15",
                    "harvest_date": "2026-08-10",
                    "status": "Зростає",
                },
                {
                    "name": "Кукурудза",
                    "variety": "Цукрова золота",
                    "field": "Південне поле",
                    "area_ha": 8.0,
                    "plant_date": "2026-04-20",
                    "harvest_date": "2026-09-05",
                    "status": "Зростає",
                    "notes": "Потребує поливу",
                },
                {
                    "name": "Картопля",
                    "variety": "Рассет",
                    "field": "Східне поле",
                    "area_ha": 4.2,
                    "plant_date": "2026-04-01",
                    "harvest_date": "2026-07-25",
                    "status": "Зібрано",
                },
            ]
        ).execute()
    if not Animal.select().exists():
        Animal.insert_many(
            [
                {
                    "animal_type": "Корова",
                    "tag_id": "C-001",
                    "breed": "Голштинська",
                    "birth_date": "2022-05-10",
                },
                {
                    "animal_type": "Корова",
                    "tag_id": "C-002",
                    "breed": "Джерсійська",
                    "birth_date": "2023-02-14",
                },
                {
                    "animal_type": "Курка",
                    "tag_id": "H-101",
                    "breed": "Род-айленд",
                    "birth_date": "2025-06-01",
                    "notes": "Несуча група",
                },
                {
                    "animal_type": "Вівця",
                    "tag_id": "S-050",
                    "breed": "Меринос",
                    "birth_date": "2024-03-20",
                    "health_status": "Потребує огляду",
                    "notes": "Злегка кульгає",
                },
            ]
        ).execute()
    if not Task.select().exists():
        today = str(date.today())
        Task.insert_many(
            [
                {
                    "title": "Полити південне поле",
                    "category": "Посіви",
                    "due_date": today,
                    "priority": "Високий",
                },
                {
                    "title": "Ветогляд S-050",
                    "category": "Тварини",
                    "due_date": today,
                    "priority": "Високий",
                },
                {
                    "title": "Замовити корм",
                    "category": "Запаси",
                    "due_date": today,
                    "priority": "Середній",
                    "done": True,
                },
            ]
        ).execute()
    if not InventoryItem.select().exists():
        InventoryItem.insert_many(
            [
                {
                    "name": "Лопата",
                    "category": "Ручні інструменти",
                    "quantity": 5,
                    "unit": "шт",
                    "condition": "Справний",
                    "location": "Склад",
                },
                {
                    "name": "Трактор МТЗ-82",
                    "category": "Техніка",
                    "quantity": 1,
                    "unit": "шт",
                    "condition": "Потребує ремонту",
                    "location": "Гараж",
                    "notes": "Заміна масла",
                },
                {
                    "name": "Насіння пшениці",
                    "category": "Насіння",
                    "quantity": 200,
                    "unit": "кг",
                    "condition": "Справний",
                    "location": "Склад",
                },
                {
                    "name": "Дизпаливо",
                    "category": "Паливо",
                    "quantity": 120,
                    "unit": "л",
                    "condition": "Справний",
                    "location": "Гараж",
                },
            ]
        ).execute()


# ---- Crops ----
def list_crops() -> list[CropRecord]:
    rows = list(Crop.select().order_by(Crop.id.desc()).dicts())
    return cast(list[CropRecord], rows)


def add_crop(
    name: str,
    variety: TextInput,
    field: TextInput,
    area_ha: NumberInput,
    plant_date: DateInput,
    harvest_date: DateInput,
    status: str,
    notes: TextInput,
) -> CropRecord:
    if not name.strip():
        raise ValueError("Назва культури обов’язкова.")
    obj = Crop.create(
        name=name.strip(),
        variety=_s(variety),
        field=_s(field),
        area_ha=_f(area_ha),
        plant_date=_d(plant_date),
        harvest_date=_d(harvest_date),
        status=status or "Зростає",
        notes=_s(notes),
    )
    _log("Посіви", "Створено", int(obj.id), name.strip())
    return CropRecord(
        id=int(obj.id),
        name=obj.name,
        variety=obj.variety,
        field=obj.field,
        area_ha=float(obj.area_ha),
        plant_date=obj.plant_date,
        harvest_date=obj.harvest_date,
        status=obj.status,
        notes=obj.notes,
    )


def update_crop(
    crop_id: int,
    name: str,
    variety: TextInput,
    field: TextInput,
    area_ha: NumberInput,
    plant_date: DateInput,
    harvest_date: DateInput,
    status: str,
    notes: TextInput,
) -> bool:
    obj = Crop.get_or_none(Crop.id == crop_id)
    if obj is None:
        return False
    obj.name = name
    obj.variety = _s(variety)
    obj.field = _s(field)
    obj.area_ha = _f(area_ha)
    obj.plant_date = _d(plant_date)
    obj.harvest_date = _d(harvest_date)
    obj.status = status or "Зростає"
    obj.notes = _s(notes)
    obj.save()
    _log("Посіви", "Оновлено", crop_id, name)
    return True


def delete_crop(crop_id: int) -> bool:
    obj = Crop.get_or_none(Crop.id == crop_id)
    if obj is None:
        return False
    name = str(obj.name)
    obj.delete_instance()
    _log("Посіви", "Видалено", crop_id, name)
    return True


# ---- Livestock ----
def list_livestock() -> list[AnimalRecord]:
    rows = list(Animal.select().order_by(Animal.id.desc()).dicts())
    return cast(list[AnimalRecord], rows)


def add_animal(
    animal_type: str,
    tag_id: TextInput,
    breed: TextInput,
    birth_date: DateInput,
    health_status: str,
    notes: TextInput,
) -> AnimalRecord:
    obj = Animal.create(
        animal_type=animal_type,
        tag_id=_s(tag_id),
        breed=_s(breed),
        birth_date=_d(birth_date),
        health_status=health_status or "Здорова",
        notes=_s(notes),
    )
    _log("Тварини", "Створено", int(obj.id), f"{animal_type} {_s(tag_id)}")
    return AnimalRecord(
        id=int(obj.id),
        animal_type=obj.animal_type,
        tag_id=obj.tag_id,
        breed=obj.breed,
        birth_date=obj.birth_date,
        health_status=obj.health_status,
        notes=obj.notes,
    )


def update_animal(
    animal_id: int,
    animal_type: str,
    tag_id: TextInput,
    breed: TextInput,
    birth_date: DateInput,
    health_status: str,
    notes: TextInput,
) -> bool:
    obj = Animal.get_or_none(Animal.id == animal_id)
    if obj is None:
        return False
    obj.animal_type = animal_type
    obj.tag_id = _s(tag_id)
    obj.breed = _s(breed)
    obj.birth_date = _d(birth_date)
    obj.health_status = health_status or "Здорова"
    obj.notes = _s(notes)
    obj.save()
    _log("Тварини", "Оновлено", animal_id, f"{animal_type} {_s(tag_id)}")
    return True


def delete_animal(animal_id: int) -> bool:
    obj = Animal.get_or_none(Animal.id == animal_id)
    if obj is None:
        return False
    details = f"{obj.animal_type} {obj.tag_id}"
    obj.delete_instance()
    _log("Тварини", "Видалено", animal_id, details)
    return True


# ---- Tasks ----
def list_tasks(only_open: bool = False) -> list[TaskRecord]:
    query = Task.select()
    if only_open:
        query = query.where(Task.done == False)  # noqa: E712
        query = query.order_by(Task.due_date)
    else:
        query = query.order_by(Task.done, Task.due_date)
    return cast(list[TaskRecord], list(query.dicts()))


def add_task(
    title: str, category: str, due_date: DateInput, priority: str, notes: TextInput
) -> TaskRecord:
    if not title.strip():
        raise ValueError("Назва завдання обов’язкова.")
    obj = Task.create(
        title=title.strip(),
        category=category or "Загальне",
        due_date=_d(due_date),
        priority=priority or "Середній",
        done=False,
        notes=_s(notes),
    )
    _log("Завдання", "Створено", int(obj.id), title.strip())
    return TaskRecord(
        id=int(obj.id),
        title=obj.title,
        category=obj.category,
        due_date=obj.due_date,
        priority=obj.priority,
        done=bool(obj.done),
        notes=obj.notes,
    )


def toggle_task(task_id: int, done: bool) -> bool:
    obj = Task.get_or_none(Task.id == task_id)
    if obj is None:
        return False
    obj.done = bool(done)
    obj.save()
    _log(
        "Завдання",
        "Перемкнуто",
        task_id,
        f"{obj.title} -> {'виконано' if done else 'відкрито'}",
    )
    return True


def delete_task(task_id: int) -> bool:
    obj = Task.get_or_none(Task.id == task_id)
    if obj is None:
        return False
    title = str(obj.title)
    obj.delete_instance()
    _log("Завдання", "Видалено", task_id, title)
    return True


# ---- Inventory ----
def list_inventory() -> list[InventoryRecord]:
    rows = list(InventoryItem.select().order_by(InventoryItem.id.desc()).dicts())
    return cast(list[InventoryRecord], rows)


def add_inventory_item(
    name: str,
    category: str,
    quantity: NumberInput,
    unit: str,
    condition: str,
    location: TextInput,
    notes: TextInput,
) -> InventoryRecord:
    if not name.strip():
        raise ValueError("Назва інвентарю обов’язкова.")
    qty = _f(quantity)
    obj = InventoryItem.create(
        name=name.strip(),
        category=category or "Інше",
        quantity=qty,
        unit=unit or "шт",
        condition=condition or "Справний",
        location=_s(location),
        notes=_s(notes),
    )
    _log("Інвентар", "Створено", int(obj.id), f"{name.strip()} ({qty} {obj.unit})")
    return InventoryRecord(
        id=int(obj.id),
        name=obj.name,
        category=obj.category,
        quantity=float(obj.quantity),
        unit=obj.unit,
        condition=obj.condition,
        location=obj.location,
        notes=obj.notes,
    )


def update_inventory_item(
    item_id: int,
    name: str,
    category: str,
    quantity: NumberInput,
    unit: str,
    condition: str,
    location: TextInput,
    notes: TextInput,
) -> bool:
    obj = InventoryItem.get_or_none(InventoryItem.id == item_id)
    if obj is None:
        return False
    obj.name = name
    obj.category = category or "Інше"
    obj.quantity = _f(quantity)
    obj.unit = unit or "шт"
    obj.condition = condition or "Справний"
    obj.location = _s(location)
    obj.notes = _s(notes)
    obj.save()
    _log("Інвентар", "Оновлено", item_id, name)
    return True


def delete_inventory_item(item_id: int) -> bool:
    obj = InventoryItem.get_or_none(InventoryItem.id == item_id)
    if obj is None:
        return False
    name = str(obj.name)
    obj.delete_instance()
    _log("Інвентар", "Видалено", item_id, name)
    return True


# ---- Logs ----
def list_logs(
    limit: int = 200, entity: str | None = None, action: str | None = None
) -> list[LogRecord]:
    query = ActivityLog.select()
    if entity:
        query = query.where(ActivityLog.entity == entity)
    if action:
        query = query.where(ActivityLog.action == action)
    query = query.order_by(ActivityLog.id.desc()).limit(limit)
    rows = cast(list[dict[str, Any]], list(query.dicts()))
    out: list[LogRecord] = []
    for r in rows:
        ca = r.get("created_at")
        out.append(
            LogRecord(
                id=int(r["id"]),
                created_at=str(ca)[:19] if ca is not None else "",
                entity=str(r.get("entity") or ""),
                action=str(r.get("action") or ""),
                entity_id=(
                    int(r["entity_id"]) if r.get("entity_id") is not None else None
                ),
                details=str(r.get("details") or ""),
            )
        )
    return out


def clear_logs() -> None:
    ActivityLog.delete().execute()
